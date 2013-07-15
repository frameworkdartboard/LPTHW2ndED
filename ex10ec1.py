# ex10ec1.py
# Let's make some flash cards!

import random

# maps escape sequences to their description
seq_to_desc = {'\\\\': 'Backslash (\\)', '\\\'': 'Single quote (\')',
              '\\"': 'Double quote (")', '\\a': 'ASCII Bell (BEL)',
              '\\b': 'ASCII Backspace (BS)', '\\f': 'ASCII Formfeed (FF)',
              '\\n': 'ASCII Linefeed (LF)', 
              '\\N{name}': 'Character named name in the Unicode database (Unicode only)',
              '\\r': 'ASCII Carriage Return (CR)', '\\t': 'ASCII Horizontal Tab (TAB)',
              '\\uxxxx': 'Character with 16-bit hex value xxxx (Unicode only)',
              '\\Uxxxxxxxx': 'Character with 32-bit hex value xxxxxxxx (Unicode only)',
              '\\v': 'ASCII Vertical Tab (VT)', '\\ooo': 'Character with octal value ooo',
              '\\xhh': 'Character with hex value hh'
             }
             
# maps descriptions of escape sequences to the escape sequences
desc_to_seq = dict((v,k) for k,v in seq_to_desc.iteritems())

sequences = seq_to_desc.keys()
descriptions = desc_to_seq.keys()

total_count = correct_count = 0

random.seed()

# setting a default answer to guarantee that the main program loop doesn't
# terminate the very first time it's run
answer = "notexit"

while True:
    direction = random.randint(0,1)
    if 0 == direction:
        seq = random.choice(sequences)
        print "Escape Sequence: %s" % seq
        answer = raw_input("Describe what this sequence does (or enter 'exit' to quit): ")
        if answer == seq_to_desc[seq]:
            print "You're right!"
            correct_count += 1
        elif answer != 'exit':
            print "You're wrong.  The right answer is \"%s\"." % seq_to_desc[seq]
    else:
        desc = random.choice(descriptions)
        print "Description: %s" % desc
        answer = raw_input("What escape sequence fits this description? (or enter 'exit' to quit): ")
        if answer == desc_to_seq[desc]:
            print "You're right!"
            correct_count += 1
        elif answer != 'exit':
            print "You're wrong.  The right answer is \"%s\"." % desc_to_seq[desc]
                       
    if 'exit' == answer:
        break
    total_count += 1

print "You answered %d out of %d questions correctly!" % (correct_count, total_count)
print "You're ratio of correct answers to total questions is %f" % (correct_count * 1.0 / total_count)
