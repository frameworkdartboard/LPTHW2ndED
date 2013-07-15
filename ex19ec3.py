def mult_string(str_to_mult, how_many):
    print str_to_mult * how_many

print "Let's try mult_string() with 'abcd' and 5: ",
mult_string ('abcd',5)

print "Let's try some more examples: "
mult_string ('dance', 7)
mult_string ('oaken' + 'fold', 2)

str_val1 = 'turbo'
str_val2 = 'charged'
num_val1 = 2
num_val2 = 3

mult_string (str_val1 + '-boost', 1)
mult_string (str_val1 + ' acid house', 3)
mult_string (str_val1, num_val1 * 6)
mult_string (str_val1 + str_val2 + ' ', 9)
mult_string ('do you copy?', num_val2 + num_val1)
mult_string ('bass' * 4, 2)
mult_string ('treble' * 2, num_val1)
mult_string ('wild out', 0)
