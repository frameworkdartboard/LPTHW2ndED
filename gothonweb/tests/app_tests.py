from nose.tools import *
import web
from bin.app import app
from tests.tools import assert_response

def login_fails_helper(b):
    b.open("/")
    # test that you get the login page
    assert_in("Login:", b.data)
    b.select_form("loginform")
    b["login"] = "asdf"
    b["apassword"] = "qwresdf"
    b.submit()
    assert_in("USER NOT FOUND", b.data)

def test_login_fails():
    b = app.browser()
    login_fails_helper(b)

def login_succeeds_helper(b):
    b.open("/")
    assert_in("Login:", b.data)
    b.select_form("loginform")
    b["login"] = "ekramer"
    b["apassword"] = "python"
    b.submit()
    assert_in("The Gothons of Planet Percal #25 have invaded your ship and destroyed",b.data)

def test_login_succeeds():
    b = app.browser()
    login_succeeds_helper(b)

def test_corridor_shoot_death():
    b = app.browser()
    login_succeeds_helper(b)

    b.select_form("myform")
    b["action"] = "shoot!"
    b.submit()
    # corridor_shoot_death 
    assert_in("Quick on the draw you yank out your blaster and fire it at the Gothon.",b.data)
    # test that you're not at an error page
    assert_not_in("I don\'t understand.  Please try another command.",b.data) 
    # test that you ARE being asked to play again (since you died)
    assert_in("Play Again?", b.data)
    # negative test
    assert_not_in("parpy",b.data)

def test_corridor_dodge_death():
    b = app.browser()
    login_succeeds_helper(b)

    b.select_form("myform")
    b["action"] = "dodge!"
    b.submit()
    # corridor_dodge_death 
    assert_in("Like a world class boxer you dodge, weave, slip and slide right",b.data)
    # test that you're not at an error page
    assert_not_in("I don\'t understand.  Please try another command.",b.data)
    # test that you ARE being asked to play again (since you died)
    assert_in("Play Again?", b.data)
    # negative test
    assert_not_in("parpy",b.data)
#
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "asdfasdfaSYNTAXERROR"
#    b.submit()
#    # central_corridor w errmsg
#    assert_in("The Gothons of Planet Percal #25 have invaded your ship and destroyed", b.data)
#    # test that you ARE at an error page
#    assert_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you're not being asked to play again
#    assert_not_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    # laser_weapon_armory
#    assert_in("Lucky for you they made you learn Gothon insults in the academy.",b.data)
#    # test that you're not at an error page
#    assert_not_in("I don\'t understand.  Please try another command.",b.data)
#    # test that you're not being asked to play again
#    assert_not_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.select_form("myform")
#    b["action"] = "01xx"
#    b.submit()
#    # armory_guess_death
#    assert_in("The lock buzzes one last time and then you hear a sickening", b.data)
#    # test that you're not at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you ARE being asked to play again (since you died)
#    assert_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "0132"
#    b.submit()
#    # the_bridge
#    assert_in("The container clicks open and the seal breaks, letting gas out.", b.data)
#    # test that you're not at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you're not being asked to play again
#    assert_not_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.select_form("myform")
#    b["action"] = "throw the bomb"
#    b.submit()
#    # bridge_throw_death
#    assert_in("In a panic you throw the bomb at the group of Gothons", b.data)
#    # test that you're not at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you ARE being asked to play again (since you died)
#    assert_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "0132"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "ERRORERRORsadf"
#    b.submit()
#    # the_bridge w error
#    assert_in("The container clicks open and the seal breaks, letting gas out.", b.data)
#    # test that you ARE at an error page
#    assert_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you're not being asked to play again
#    assert_not_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.select_form("myform")
#    b["action"] = "slowly place the bomb"
#    b.submit()
#    # escape_pod
#    assert_in("You point your blaster at the bomb under your arm", b.data)
#    # test that you aren't at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you're not being asked to play again
#    assert_not_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.select_form("myform")
#    b["action"] = "3"
#    b.submit()
#    # the_end_loser
#    assert_in("You jump into a random pod and hit the eject button.", b.data)
#    # test that you aren't at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you ARE being asked to play again (since you died)
#    assert_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#    
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "0132"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "slowly place the bomb"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "asdf"
#    b.submit()
#    # the_end_loser w not even a valid pod #
#    assert_in("You jump into a random pod and hit the eject button.", b.data)
#    # test that you aren't at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you ARE being asked to play again (since you died)
#    assert_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
#
#    b.open("/")
#    b.select_form("myform")
#    b["action"] = "tell a joke"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "0132"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "slowly place the bomb"
#    b.submit()
#    b.select_form("myform")
#    b["action"] = "2"
#    b.submit()
#    # the_end_winner
#    assert_in("You jump into pod 2 and hit the eject button.", b.data)
#    # test that you aren't at an error page
#    assert_not_in("I don\'t understand.  Please try another command.", b.data)
#    # test that you ARE being asked to play again (since YOU WON!)
#    assert_in("Play Again?", b.data)
#    # negative test
#    assert_not_in("parpy",b.data)
