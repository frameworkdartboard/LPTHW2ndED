from nose.tools import *
import web
from loginexperiment.loginexperiment import app
from tests.tools import assert_response

def test_the_whole_loginexperiment_enchilada():

    b = app.browser()
    b.open("/")

    # login screen should be the first screen
    assert_in("Testing Index",b.data)
#
#    # first try wrong username and wrong password
#    b.select_form("loginform")
#    b["login"] = "eclamer"
#    #b["password"] = ""
#    b.submit()
#
#    # should bring up the user not found screen
#    assert_in("USER NOT FOUND",b.data)
