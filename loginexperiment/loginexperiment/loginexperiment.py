import hashlib
import sqlite3
import web

urls = (
  '/', 'Index',
  '/index', 'Index',
  '/game', 'Game'
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
        pwdhash = hashlib.md5(i.apassword).hexdigest()
        cursor = authdb.execute('select * from users where login=? and password=?', (i.login, pwdhash))

        row = cursor.fetchone()
        if row:
            check = row[0]
        else:
            check = None

        # DEBUG = off print "check: '%r'" % check
        if check:
            session.loggedin = True
            session.login = i.login
            #raise web.seeother('/game')
            return render.game()
        else: 
            return render.usernotfound()

class Game(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        # session.room = map.START
        session.room = "thisisatest" # the full session test will set this too
        session.syntaxerror = False
        return render.game()

if __name__ == "__main__":
    app.run()
