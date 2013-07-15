class Fartknocker(object):

    army = "this fartknocker's army"

print "Fartknocker.army: %r" % Fartknocker.army
print ""
print "hasattr(Fartknocker, 'army') == %r" % hasattr(Fartknocker, 'army')
print "hasattr(Fartknocker, 'navy') == %r" % hasattr(Fartknocker, 'navy')
print ""
setattr(Fartknocker, 'navy', "oh sweet georgia brown, now this fartknocker's got a navy too.")
print "setattr(Fartknocker, 'navy', \"oh sweet georgia brown, now this fartknocker's got a navy too.\")"
print ""
print "Fartknocker.army: %r" % Fartknocker.army
print "Fartknocker.navy: %r" % Fartknocker.navy
print ""
print "hasattr(Fartknocker, 'army') == %r" % hasattr(Fartknocker, 'army')
print "hasattr(Fartknocker, 'navy') == %r" % hasattr(Fartknocker, 'navy')
