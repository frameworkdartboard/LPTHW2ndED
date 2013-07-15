# instead of going straight to a print statement, this shows that you can set a variable to a string value made out of a string with a field format in it followed by a value for the field using the % operator
x = "There are %d types of people." % 10
# one string to fill in a string field specifier included in a bigger string.
binary = "binary"
# another string to fill in a string field specifier in a bigger string.
do_not = "don't"
# this shows that when you have more than field specifier, the values that fill them in must come from a list surrounded by parentheses.
y = "Those who know %s and those who %s." % (binary, do_not)
# DOES THIS COUNT AS ONE PLACE OR TWO?
# printing the stored string value that was built with field specifiers
print x
# the same thing as above
print y

# printing the stringified object which even includes the delimiters (single quote or double quote)
print "I said: %r." % x
# Now including yet another string that itself included a smaller string.
print "I also said: '%s'." % y
# This could be 3 and 4
# Stores what is probably going to turn out to be a boolean value of False
hilarious = False
# Stores a string with a formatted field.
joke_evaluation = "Isn't that joke so funny?! %r"
# But what if this is 5?
# Uses the stored boolean and the string with a formatted field ready to be filled.  Uses the boolean to fill in the formatted field.
print joke_evaluation % hilarious

# These last 3 lines are used to demonstrate string concatenation.  It looks like, unlike the comma operator, it doesn't add an un-asked for space.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
# does this work?
print w, e

# Haha, it does, and you do get an unasked for space again!

# My explanation is that the plus sign, when operating on a string and a string, makes a bigger string out of the two earlier strings.
