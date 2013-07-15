# imports the argv object specifically from the sys module rather than requiring the whole module
from sys import argv

# unpacks args from command line and gives them names that are easier to remember
script, input_file = argv

# defines a function that (apparently) prints the entire file.  notes: 1. it depends on receiving a file handle rather than a file name, 2. it doesn't test the file handle for validity.  it just goes ahead.
def print_all(f):
    # the actual command that prints the entire file.
    print f.read()

# sets the pointer in the file handle back to the start of the file
def rewind(f):
    # 0 represents the start of the file
    f.seek(0)

# prints a number and prints one line
def print_a_line(line_count, f):
    # it's not actually corelating the line # to the location of the file pointer
    # also: readline() on a file handle must set the file pointer because it can
    # be run repeatedly to get one line after another instead of the same line
    # over and over again
    print line_count, f.readline()

# creates a file handle based on the file name from the prompt (Doesn't check if file exists!)
current_file = open(input_file)

# I tell you what I'm going to do...
print "First let's print the whole file:\n"

# Uses that function we created above to barf it all out.
print_all(current_file)

# Rewinds the file pointer that is a property of the file handle back to the beginning
print "Now let's rewind, kind of like a tape."

# Yeah, like I said.
rewind(current_file)

# Print three lines
print "Let's print three lines:"

# set line counter to 1
current_line = 1
# print a line that matches the counter
print_a_line(current_line, current_file)

# increment the counter
current_line = current_line + 1
# print the next line which matches the counter
print_a_line(current_line, current_file)

# increment the counter again
current_line = current_line + 1
# print the next line which matches counter
print_a_line(current_line, current_file)
