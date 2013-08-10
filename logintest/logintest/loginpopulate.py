import hashlib
import web
import sqlite3

print "LOGINTEST"
authdb = sqlite3.connect('users.db')

c = authdb.cursor()

#CREATE TABLE t(x INTEGER PRIMARY KEY ASC, y, z);
# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()

#c.execute("CREATE TABLE users (login text PRIMARY KEY, password text, hiscore integer)")
#
#md5_hashed_passwd = (hashlib.md5('python').hexdigest(),)
#c.execute("INSERT INTO users VALUES ('ekramer', ?, 0)", md5_hashed_passwd)
#
#md5_hashed_passwd = (hashlib.md5('java').hexdigest(),)
#c.execute("INSERT INTO users VALUES ('bkramer', ?, 0)", md5_hashed_passwd)

authdb.commit()

authdb.close()

authdb = sqlite3.connect('users.db')

c = authdb.cursor()

for row in c.execute('SELECT * FROM users'):
    print row

authdb.commit()

authdb.close()
