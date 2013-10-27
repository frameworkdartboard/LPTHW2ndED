import sqlite3
import hashlib

def isUserValid (login, password):
    authdb = sqlite3.connect('users.db')
    pwdhash = hashlib.md5(password).hexdigest()
    cursor = authdb.execute('select * from users where login=? and password=?', (login, pwdhash))

    row = cursor.fetchone()
    if row:
        return True
    else:
        return False
