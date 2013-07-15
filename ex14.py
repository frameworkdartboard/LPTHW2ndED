from sys import argv

script, first_name, last_name = argv
prompt = '==>'

print "Hi %s %s, I'm the %s script." % (first_name, last_name, script)
print "I'd like to ass you a few questions."
print "Do you like me %s, %s?" % (last_name, first_name)
likes = raw_input(prompt)

print "Where do you live %s, %s?" % (last_name, first_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, %s, %s, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (last_name, first_name, likes, lives, computer)
