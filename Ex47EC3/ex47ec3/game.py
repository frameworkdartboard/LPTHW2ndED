# game.py
import items
import rooms

class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Game(object):

    def __init__(self):
        self.these_rooms = rooms.room_list
        self.these_items = items.item_list
        self.state = { "has_sword": False, "has_helm": False }
        self.cur_room_name = rooms.starting_room
        self.cur_room = self.these_rooms[self.cur_room_name]
        
    def show_room_attribs(self, room_name):
        cur_room = self.these_rooms[room_name]
        print ""
        print "Short Name: %r" % cur_room.shortname
        print "Long Name: %r" % cur_room.longname
        print "Descriptions: %r" % cur_room.desc
        print "Exits: %r" % cur_room.exits
        print "Items: %r" % cur_room.items
        print "Foes: %r" % cur_room.foes
        
    def show_all_room_attribs(self):
        for ii in self.these_rooms.keys():
            self.show_room_attribs(ii)

    def show_all_item_attribs(self):
        for ii in self.these_items.keys():
            print ""
            print "Short Name: %r" % self.these_items[ii].shortname
            print "Long Name: %r" % self.these_items[ii].longname
            print "Description: %r" % self.these_items[ii].desc


    def fight(self):
        msg = ""
        gameover = True
        
        if not self.state["has_sword"]:
            msg = clr.FAIL + ("The %s slays you!  You are slain!  If only you had a sword." % self.cur_room.foes[0]) + clr.ENDC
        elif self.cur_room.foes[0] == "green_ogre":
            if not self.state["has_helm"]:
                msg = clr.FAIL + "The green ogre slays you!  You are slain!  If only you had some armor, maybe a helmet." + clr.ENDC
            else:
                msg = clr.OKGREEN + \
"""
The green ogre utters 'my time here is *ogre*' and then 
succumbs to his injuries. So tragic!
You are victorious!  Hooray. 
"""             + clr.ENDC

        else:
            msg = clr.OKGREEN + "You hack the %s to death with your sword.  You've won this round!" % self.cur_room.foes[0] + clr.ENDC
            self.cur_room.foes = []
            gameover = False
        return [msg, gameover]


    def get_item(self):
        the_item = self.cur_room.items[0]
        print clr.OKGREEN + ("You pick up the %s." % the_item) + clr.ENDC

        if the_item == "singing_sword":
            self.state["has_sword"] = True
            print clr.OKGREEN + "The sword sings in your hand!" + clr.ENDC
        elif the_item == "wolf_head":
            self.state["has_helm"] = True
            print clr.OKGREEN + "The wolf's head makes a sturdy helm!" + clr.ENDC

        self.cur_room.items = []

    def play_the_game(self):
        command = ""
        
        while True:
            self.show_room_attribs(self.cur_room_name)
            command = raw_input(clr.OKBLUE + "Enter a command: " + clr.ENDC)
            command = command.lower()

            if command in ["exit","q","quit"]:
                print clr.FAIL + "Quitter!" + clr.ENDC
                break

            if self.cur_room.foes and command == "fight":
                [msg, gameover] = self.fight()
                print msg
                if gameover:
                    exit()
            elif command in self.cur_room.exits:
                self.cur_room_name = command
                self.cur_room = self.these_rooms[self.cur_room_name]
            elif command in self.cur_room.items:
                self.get_item()
            else:
                print clr.FAIL + "I don't know what that means... " + clr.ENDC
