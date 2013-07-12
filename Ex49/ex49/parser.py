class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subj_num, subject, verb, obj_num, object):
        # remember we take ('noun','princess') tuples and convert them
        self.subj_num = subj_num[1]
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj_num = obj_num[1]
        self.object = object[1]
 
    def __eq__(self, other):
        if self.subject == other.subject and self.verb == other.verb and \
         self.object == other.object:
            return True
        else:
            return False


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')
    next = peek(word_list)

    if next == 'number':
        obj_num = match(word_list, 'number')
        next = peek(word_list)
    else:
        obj_num = ('number', 1)
    if next == 'noun':
        return (obj_num, match(word_list, 'noun'))
    if next == 'direction':
        return (obj_num, match(word_list, 'direction'))
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj_num, subj):
    verb = parse_verb(word_list)
    (obj_num, obj) = parse_object(word_list)

    return Sentence(subj_num, subj, verb, obj_num, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')

    start = peek(word_list)

    if start == 'number':
        subj_num = match(word_list, 'number')
        start = peek(word_list)
    else:
        subj_num = ('number', 1)
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj_num, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, subj_num, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)

