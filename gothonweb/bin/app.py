import web
from gothonweb import map

urls = (
  '/', 'Index',
  '/login', 'Login',
  '/usernotfound', 'UserNotFound',
  '/game', 'GameEngine',
  '/logout', 'Logout',
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

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # if a user is logged in and goes to "/" they should get sent back to the game
        # if a user is not logged in and goes to "/" they should get sent to the login page
        if session.loggedinuser == None:
            web.seeother("/login")
        else: 
            web.seeother("/game")

class Login(object):
    def GET(self):
        if session.loggedinuser != None:
            web.seeother("/game")

        
        # this is used to "setup" the session with starting values
        session.room = map.START
        session.syntaxerror = False
        web.seeother("/game")

class UserNotFound(object):
    def GET(self):
        web.seeother("/game")

class GameEngine(object):

    def GET(self):
        if session.room:
            if session.syntaxerror:
                 return render.show_room_w_error(room=session.room)
            else:
                 return render.show_room(room=session.room)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        #if we somehow lost track of the room i really don't know what else to do.
        #we must tell the world.  throw an exception!
        if not session.room:
            raise Exception("session.room is null!")

        temproom = session.room.go(form.action)
        if temproom:
            session.room = temproom
            session.syntaxerror = False
        else:
            temproom = session.room.go('*')
            if temproom:
                session.room = temproom
                session.syntaxerror = False
            else:
                session.syntaxerror = True

        web.seeother("/game")

class Logout(object):
    def GET(self):
        web.seeother("/game")

if __name__ == "__main__":
    app.run()
