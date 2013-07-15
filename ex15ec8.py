# imports the sys object from the argv module
from sys import argv

# gets arg0 and 1 from command line, doesn't count number of args
script, filename = argv

# opens a file for, at least, reading
txt = open(filename)

# tells you the name of the file that it's opening
print "Here's your file %r:" % filename
# reads from the open file handle, immediately passes that output to the "print" command, which prints it
print txt.read()
# closes the file handle now that it's not needed anymore
txt.close()

# Now you get to potentially misspell the filename yourself1!!
print "Type the filename again:"
# Here's the prompt and the save in the same line
file_again = raw_input("> ")

# Now the attempt to get a file handle for (at least) read access
txt_again = open(file_again)

# reads from the file handle and prints the result
print txt_again.read()
# closes the file handle now that it's not needed anymore
txt.close()
