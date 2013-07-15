# prints mary had a little lamb.  simple string literal
print "Mary had a little lamb."
# prints Its fleece was white as snow.  It turns out that you can simply supply another string to a field using the % operator.
print "Its fleece was white as %s." % 'snow'
# prints another constant string
print "And everywhere that Mary went."
# looks like it does for concatenation what multiplication does for addition.  it iterates it finitely.  pretty cool
print "." * 10  # what'd that do?

# print "creates a one character string"
end1 = "C"
# print "creates a one character string"
end2 = "h"
# print "creates a one character string"
end3 = "e"
# print "creates a one character string"
end4 = "e"
# print "creates a one character string"
end5 = "s"
# print "creates a one character string"
end6 = "e"
# print "creates a one character string"
end7 = "B"
# print "creates a one character string"
end8 = "u"
# print "creates a one character string"
end9 = "r"
# print "creates a one character string"
end10 = "g"
# print "creates a one character string"
end11 = "e"
# print "creates a one character string"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# looks like you can suppress carriage returns at the end of supplied strings using a comma, then the results of the next print statement come in behind it
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
