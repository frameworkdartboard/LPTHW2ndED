my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs

cms_per_inch = 2.54
lbs_per_kilo = 2.2

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "but he's also %f cm tall." % (my_height * cms_per_inch)
print "He's %d pounds heavy." % my_weight
print "but he's also %f kgs heavy." % (my_weight / lbs_per_kilo)
print "Actually that's not too heavy."
