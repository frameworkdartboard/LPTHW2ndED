def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
def return2():
    return 2
    
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# ec2 translate to formula: (30 + 5) + (78 - 4) - ((90 * 2) * ((100 / 2) / 2))
# 35 + 74 = 109, 109 - (180 * 25) = 109 - 4500 = -4391
# ec3 let's calculate new things!: 2 + 2 * (9 - (4.0 / 3.0) (which should be 4 * 7.6666666
# = 28 + 0.666666 * 4 = 28 + 2/3 * 4 = 28 + 8/3 = 30 + 2/3 = 30.6666
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what = multiply(add(2, 2), subtract(9, divide(4.0, 3.0)))

print "That becomes: ", what, "Can you do it by hand?"

