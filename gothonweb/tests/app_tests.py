from nose.tools import *
import web
from bin.app import app
from tests.tools import assert_response

def test_the_whole_gothon_enchilada():

    b = app.browser()
    b.open("/")
    # central_corridor
    assert_in("The Gothons of Planet Percal #25 have invaded your ship and destroyed",b.data)
    # test that you're not at an error page
    assert_not_in("I don\'t understand.  Please try another command.", b.data)
    # negative test
    assert "parpy" not in b.data

    b.select_form("myform")
    b["action"] = "shoot!"
    b.submit()
    # corridor_shoot_death 
    assert "Quick on the draw you yank out your blaster and fire it at the Gothon." in b.data
    # test that you're not at an error page
    assert "I don\'t understand.  Please try another command."    
    # negative test
    assert "parpy" not in b.data

    b.open("/")
    b.select_form("myform")
    b["action"] = "dodge!"
    b.submit()
    # corridor_dodge_death 
    assert "Like a world class boxer you dodge, weave, slip and slide right" in b.data
    # test that you're not at an error page
    assert "I don\'t understand.  Please try another command." not in b.data
    # negative test
    assert "parpy" not in b.data

    b.open("/")
    b.select_form("myform")
    b["action"] = "tell a joke"
    b.submit()
    # laser_weapon_armory
    assert "Lucky for you they made you learn Gothon insults in the academy." in b.data
    # test that you're not at an error page
    assert "I don\'t understand.  Please try another command." not in b.data
    # negative test
    assert "parpy" not in b.data

    b.open("/")
    b.select_form("myform")
    b["action"] = "asdfasdfaSYNTAXERROR"
    b.submit()
    # central_corridor w errmsg
    assert "The Gothons of Planet Percal #25 have invaded your ship and destroyed" in b.data
    # test that you ARE at an error page
    assert_in("I don\'t understand.  Please try another command.", b.data)
    # negative test
    assert "parpy" not in b.data

#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "01xx"
#    # armory_guess_death
#    assert "The lock buzzes one last time and then you hear a sickening" in b.data
#    # test that you're not at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # negative test
#    assert "parpy" not in b.data
