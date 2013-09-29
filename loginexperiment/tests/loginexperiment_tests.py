from nose.tools import *
import web
from loginexperiment.loginexperiment import app
from tests.tools import assert_response

def test_the_whole_loginexperiment_enchilada():

    b = app.browser()
    b.open("/")

    # login screen should be the first screen
    assert_in("Testing Index",b.data)

    # first try wrong username and wrong password
    b.select_form(name="loginform")
    b["login"] = "eclamer"
    b["apassword"] = ""
    b.submit()

    # should bring up the user not found screen
    assert_in("USER NOT FOUND",b.data)
    b.follow_link(text="Go back")

    # should be back at first screen
    assert_in("Testing Index",b.data)
    
    # 2nd try right username and wrong password
    b.select_form(name="loginform")
    b["login"] = "ekramer"
    b["apassword"] = "NOPE"
    b.submit()

    # should bring up the user not found screen
    assert_in("USER NOT FOUND",b.data)
    b.follow_link(text="Go back")

    # 3rd try right username and right password
    b.select_form(name="loginform")
    b["login"] = "ekramer"
    b["apassword"] = "python"
    b.submit()

    # should bring up the game screen
    assert_in("INSERT GAME HERE",b.data)
