# rooms.py

class antechamber(object):

    def __init__(self):
        self.shortname = "antechamber"
        self.longname = "The Antechamber"
        self.desc = "This is the Antechamber.  Your adventure awaits!"
        self.exits = ["room_full_o_skulls"]
        self.items = []
        self.foes = []
        
class room_full_o_skulls(object):

    def __init__(self):
        self.shortname = "room_full_o_skulls"
        self.longname = "Room Full O' Skulls"
        self.desc = "This room is packed to the rafters with skulls.  That isn't intimidating.  Nope!  Not at all!"
        self.exits = ["antechamber","armory"]
        self.items = []
        self.foes = []
        
class armory(object):

    def __init__(self):
        self.shortname = "armory"
        self.longname = "Armory"
        self.desc = "Swords, scimitars, and flails glisten from the walls.  You can probably do some major damage with something in this room."
        self.exits = ["room_full_o_skulls", "great_hall"]
        self.items = ["singing_sword"]
        self.foes = []
        
class great_hall(object):

    def __init__(self):
        self.shortname = "great_hall"
        self.longname = "Great Hall"
        self.desc = "The centre of the castle.  The vaulted ceiling almost seems to disappear in the darkness above.  This castle is really big."
        self.exits = ["armory", "tapestry_room", "treasure_room"]
        self.items = []
        self.foes = ["gelatinous_cube"]
        
class tapestry_room(object):

    def __init__(self):
        self.shortname = "tapestry_room"
        self.longname = "Tapestry Room"
        self.desc = "You are in the tapestry room.  Beautiful and detailed tapestries deck the halls."
        self.exits = ["great_hall", "blackwater_park"]
        self.items = ["wolf_head"]
        self.foes = []
        
class blackwater_park(object):

    def __init__(self):
        self.shortname = "blackwater_park"
        self.longname = "Blackwater Park"
        self.desc = '"Sick liaisons raised this monumental mark / The sun sets forever over Blackwater park."'
        self.exits = ["tapestry_room"]
        self.items = []
        self.foes = ["sharktopus"]
        
class treasure_room(object):

    def __init__(self):
        self.shortname = "treasure_room"
        self.longname = "Treasure Room"
        self.desc = "Look daddy a treasure.  A treasure!!!"
        self.exits = ["ogre_room", "great_hall"]
        self.items = ["bag_full_o_gold"]
        self.foes = []

class ogre_room(object):

    def __init__(self):
        self.shortname = "ogre_room"
        self.longname = "Ogre Room"
        self.desc = "Huge piles of skellington bones fill this room. Be on your guard!"
        self.exits = ["treasure_room"]
        self.items = []
        self.foes = ["green_ogre"]
        
room_list = { 
    "antechamber": antechamber(), "room_full_o_skulls": room_full_o_skulls(), "armory": armory(),
    "great_hall": great_hall(), "tapestry_room": tapestry_room(), "blackwater_park": blackwater_park(),
    "treasure_room": treasure_room(), "ogre_room": ogre_room()
}

starting_room = "antechamber"
