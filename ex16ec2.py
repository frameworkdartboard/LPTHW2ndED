from sys import argv

filename = "./test.txt"
script, filename = argv

print "Reading %s ...." % filename
thefile = open(filename)
print thefile.read()
print "Did you enjoy reading that?  I did!"
