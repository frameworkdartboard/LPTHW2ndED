# defines the function and the list of arguments it accepts
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints out the 1st arg
    print "You have %d cheeses!" % cheese_count
    # prints out the 2nd arg
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints out hooray more padding, look apostrophes don't need escapes!
    print "Man that's enough for a party!"
    # prints more padding look a newline!
    print "Get a blanket.\n"
    
# tell them what we are about to tell them like a good preacher    
print "We can just give the function numbers directly:"
# now we call the function that was defined above
cheese_and_crackers(20, 30)

# tell them what we are about to tell them like a good preacher    
print "OR, we can use variables from our script:"
# set 1st var as a positive integer
amount_of_cheese = 10
# set 2nd var asd a positive integer.  these are both plausible quantities of foodstuffs
amount_of_crackers = 50

# here's the function call, the variables are passed as the function arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# tell them what we are about to tell them like a good preacher    
print "We can even do math inside too:"
# function call, we're asking the parser to find the value of math expressions, and pass those as function arguments this time
cheese_and_crackers(10 + 20, 5 + 6)

# tell them what we are about to tell them like a good preacher    
print "And we can combine the two, variables and math:"
# function call, the parser is getting the values of the args, doing math with integer literals, then using them for the function calls.  i think zed is trying to talk about what c programmers refer to as expressions.  anything that acceptable on the right side of a single equal sign (an rvalue?)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
