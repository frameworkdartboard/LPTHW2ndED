import copy
from nose.tools import *
from ex47ec3 import rooms, game

class TestClass:
    def setup(self):
        self.the_game = game.Game()
    
    def test_room_structure(self):
        assert rooms.starting_room == 'antechamber'
        assert "room_full_o_skulls" in rooms.room_list['antechamber'].exits
        assert "antechamber" and "armory" in rooms.room_list['room_full_o_skulls'].exits
        assert "room_full_o_skulls" and "great_hall" in rooms.room_list['armory'].exits
        assert "armory" and "tapestry_room" and "treasure_room" in rooms.room_list['great_hall'].exits
        assert "great_hall" and "blackwater_park" in rooms.room_list['tapestry_room'].exits
        assert "tapestry_room" in rooms.room_list['blackwater_park'].exits
        assert "ogre_room" and "great_hall" in rooms.room_list['treasure_room'].exits
        assert "treasure_room" in rooms.room_list['ogre_room'].exits

    def test_room_contents(self):
        assert rooms.room_list['antechamber'].items == []
        assert rooms.room_list['room_full_o_skulls'].items == []
        assert "singing_sword" in rooms.room_list['armory'].items
        assert rooms.room_list['great_hall'].items == []
        assert "wolf_head" in rooms.room_list['tapestry_room'].items
        assert rooms.room_list['blackwater_park'].items == []
        assert "bag_full_o_gold" in rooms.room_list['treasure_room'].items
        assert rooms.room_list['ogre_room'].items == []

    def test_room_foes(self):
        assert rooms.room_list['antechamber'].foes == []
        assert rooms.room_list['room_full_o_skulls'].foes == []
        assert rooms.room_list['armory'].foes == []
        assert "gelatinous_cube" in rooms.room_list['great_hall'].foes
        assert rooms.room_list['tapestry_room'].foes == []
        assert "sharktopus" in rooms.room_list['blackwater_park'].foes
        assert rooms.room_list['treasure_room'].foes == []
        assert "green_ogre" in rooms.room_list['ogre_room'].foes

    def test_get_sword(self):
        gm = self.the_game
        armory_copy = copy.deepcopy(rooms.room_list['armory'])
        gm.cur_room = armory_copy
        assert gm.state['has_sword'] == False
        assert "singing_sword" in gm.cur_room.items
        gm.get_item()
        assert gm.state['has_sword'] == True
        assert gm.cur_room.items == []

    def test_get_helm(self):
        gm = self.the_game
        tapestry_copy = copy.deepcopy(rooms.room_list['tapestry_room'])
        gm.cur_room = tapestry_copy
        assert gm.state['has_helm'] == False
        assert "wolf_head" in gm.cur_room.items
        gm.get_item()
        assert gm.state['has_helm'] == True
        assert gm.cur_room.items == []

    def test_fight(self):
        gm = self.the_game
        gm.state['has_sword'] = True
        gm.state['has_helm'] = True
        great_hall_copy = copy.deepcopy(rooms.room_list['great_hall'])
        gm.cur_room = great_hall_copy
        [msg, gameover] = gm.fight()
        assert msg == game.clr.OKGREEN + "You hack the gelatinous_cube to death with your sword.  You've won this round!" + game.clr.ENDC
        assert gameover == False

    def teardown(self):
        pass
