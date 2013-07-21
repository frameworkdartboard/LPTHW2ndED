from nose.tools import *
import web
from bin.app import app
from tests.tools import assert_response

def test_index():
    web.config.debug = False

    resp = app.request("/")
    assert_response(resp, status='303 See Other')
   
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, contains="Lucky for you")

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
