from nose.tools import *
import web
from bin.app import app
from tests.tools import assert_response

def test_the_whole_gothon_enchilada():

    b = app.browser()
    b.open("/")
    # central_corridor
    assert "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
    # negative test
    assert "parpy" not in b.data

    b.select_form("myform")
    b["action"] = "shoot!"
    b.submit()
    # corridor_shoot_death 
    assert "Quick on the draw you yank out your blaster and fire it at the Gothon." in b.data

    b.open("/")
    b.select_form("myform")
    b["action"] = "tell a joke"
    b.submit()
    # laser_weapon_armory
    assert "Lucky for you they made you learn Gothon insults in the academy." in b.data

#  
#    resp = app.request("/")
#    assert_response(resp, status='303 See Other')
#   
#    data = {'action': 'tell a joke'}
#    resp = app.request("/game", method="POST", data=data)
#    assert_response(resp, contains="Lucky for you")
#
    # test our first GET request to /hello
#    resp = app.request("/game")
#    assert_response(resp)

    # test if 
#    resp = app.request("/hello", method="POST")
#    assert_response(resp, contains="Nobody")
#
#    # test that we get expected values
#    data = {'name': 'Zed', 'greet': 'Hola'}
#    resp = app.request("/hello", method="POST", data=data)
#    assert_response(resp, contains="Zed")
