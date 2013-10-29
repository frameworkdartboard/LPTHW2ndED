import web
from gothonweb import map
from websecurity import websecurity

urls = (
  '/', 'Index',
  '/login', 'Login',
  '/usernotfound', 'UserNotFound',
  '/game', 'GameEngine',
  '/logout', 'Logout',
  '/reset', 'Reset',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    # when you begin the user shouldn't be logged in, there should be no syntax error, and there
    # shouldn't be in any room yet
    session = web.session.Session(app, store,
                                  initializer={'room': None, 'syntaxerror': False, 'loggedinuser': None})
    web.config._session = session
else:
    session = web.config._session

renderwtemplate = web.template.render('templates/', base="layout")
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        # if a user is logged in and goes to "/" they should get sent back to the game
        # if a user is not logged in and goes to "/" they should get sent to the login page
        print "session.loggedinuser == '%r'." % session.loggedinuser
        if session.loggedinuser == None:
            web.seeother("/login")
        else: 
            web.seeother("/game")

class Login(object):
    def GET(self):
        return render.login()
    def POST(self):
        i = web.input()

        if websecurity.isUserValid(i.login, i.apassword):
            session.loggedinuser =  i.login
            session.room = map.START
            session.syntaxerror = False
            web.seeother("/game")
        else:
            web.seeother("/usernotfound")

class UserNotFound(object):
    def GET(self):
        return render.usernotfound()

class GameEngine(object):

    def GET(self):
        #if we somehow lost track of the room i really don't know what else to do.
        #we must tell the world.  throw an exception!
        if not session.room:
            raise Exception("GameEngine.GET(): session.room is null!")

        return self.cake_or_death(session.room)

    def POST(self):
        form = web.input(action=None)

        #if we somehow lost track of the room i really don't know what else to do.
        #we must tell the world.  throw an exception!
        if not session.room:
            raise Exception("GameEngine.POST(): session.room is null!")

        # if at least one path for a room is labelled "*" then there can't be a syntax error for it.
        temproom = session.room.go(form.action)
        if temproom:
            session.room = temproom
            return self.cake_or_death(session.room)
        else:
            temproom = session.room.go('*')
            if temproom:
                session.room = temproom
                return self.cake_or_death(session.room)
            else:
                return renderwtemplate.show_room_w_error(room=session.room)

    def cake_or_death(self,room):
        if room.name == "You died.":
            return renderwtemplate.show_room_w_death(room=room)
        else:
            return renderwtemplate.show_room(room=room)

class Logout(object):
    def GET(self):
        session.loggedinuser = None
        return render.logout()

class Reset(object):
    def GET(self):
        session.room = map.START
        web.seeother("/game")

if __name__ == "__main__":
    app.run()
