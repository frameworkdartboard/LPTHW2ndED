lexmap = {
  'north': 'direction', 'south': 'direction', 'east': 'direction', 'west': 'direction',
  'go': 'verb', 'kill': 'verb', 'eat': 'verb', 'stole': 'verb',
  'the': 'stop', 'in': 'stop', 'of': 'stop', 'a': 'stop',
  'bear': 'noun', 'princess': 'noun', 'door': 'noun', 'dumbbell': 'noun',
  'lexluthor': 'noun', 'cakes': 'noun', 'lexluthors': 'noun', 'cake': 'noun'
}

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def get_lex_tuple(s):
    try:
        slower = s.lower()
        return (lexmap[slower], slower)
    except KeyError:
        return ('error', s)

def scan(input):
    input_split = input.split()
    result = []
    for token in input_split:
        maybe_num = convert_number(token)
        if None == maybe_num:
            result.append(get_lex_tuple(token))
        else:
            result.append(('number',maybe_num))

    return result 
