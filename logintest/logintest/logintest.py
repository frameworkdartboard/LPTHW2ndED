import hashlib
import web

urls = (
  '/', 'Index',
  '/', 'Results',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None, 'syntaxerror': False})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.indextemplates()
    def POST(self):
        i = web.input()
        authdb = sqlite3.connect('users.db')
        pwdhash = hashlib.md5(i.password).hexdigest()
        check = authdb.execute('select * from users where username=? and password=?', (i.username, pwdhash))
        if check:
            session.loggedin = True
            session.username = i.username
            raise web.seeother('/results')
        else: return render.base("Those login details don't work.")

class Results(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        session.syntaxerror = False
        web.seeother("/game")

if __name__ == "__main__":
    app.run()
