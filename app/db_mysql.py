import MySQLdb as db
import app.utils as utils
from app.settings import settings

def getConnection():
    return db.connect(
        host = settings['host'],
        port = settings['port'],
        user = settings['user'],
        passwd = settings['passwd'],
        db = settings['db']
    )

class Cursor():
    def __enter__(self):
        conn = getConnection()
        self.cursor = conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        if traceback:
            print "Type: ",type
            print "Value: ", value
            print "Trace: ", traceback
        return not traceback

def fetchone(cursor):
    # return a dict with col names appended to results
    row = cursor.fetchone()
    if row is None: return None

    cols = [ desc[0] for desc in cursor.description ]
    return dict(zip(cols, row))

def fetchall(cursor):
    # return a dict with col names appended to results
    results = cursor.fetchall()

    if results is None: return None

    cols = [desc[0] for desc in cursor.description ]
    ret = []

    for row in results:
        ret.append(dict(zip(cols, row)))

    return ret

#--------------- Videos-------------------------------------------------
def getAllVideos():
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos')
        return fetchall(cursor)


def getVideo(pk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos where pk=%s', (pk, ))
        return fetchone(cursor)

#--------------- Notes -------------------------------------------------
def getNotesForVideo(vid_fk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s', (vid_fk,))
        return fetchall(cursor)

def getNotes(video_fk, username):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s and user=%s', (video_fk, username))
        return fetchall(cursor)

def getSharedNotes(video_fk):
    with Cursor as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s and share=1')
        return fetchall(cursor);

def addNote(vid_fk, time, text, user):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notes (vid_fk, time, text, user)
        VALUES (%s, %s, %s, %s)
        ''', (vid_fk, time, text, user))
    conn.commit()
    note_pk = cursor.lastrowid
    return {'id': note_pk}

def deleteNote(note_pk):
    conn = getConnection()
    conn.cursor().execute('''
        DELETE FROM notes where pk = %s
    ''', (note_pk,))
    conn.commit()

def updateNote(note_pk, time, text):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE notes
        SET text=%s, time=%s
        WHERE pk= %s
        ''', (text, time, note_pk))
    conn.commit()

def isAuthor(note_pk, user):
    with Cursor() as cursor:
        cursor.execute('SELECT COUNT(*) from notes where pk=%s and user=%s', (note_pk, user))
        return True if cursor.fetchone()[0] == 1 else False


#--------------- Users -------------------------------------------------
def getUserByName(name):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM users where username=%s', (name,))
        return cursor.fetchone()

def authUser(name, password):
    pwd = utils.encrypt(password)
    with Cursor() as cursor:
        cursor.execute("""
            SELECT * FROM users
            WHERE username=%s
            AND password=%s
            """, (name, pwd))
        return cursor.fetchone()


def checkUserNameExists(name):
    with Cursor() as cursor:
        cursor.execute('''
          SELECT COUNT(*) FROM users
          where username = %s
        ''', (name,))
        return True if cursor.fetchone()[0] == 1 else False

def registerUser(name, password, email):
    pwd = utils.encrypt(password)
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
          INSERT INTO USERS(username, password, email)
          values (%s, %s, %s)
        ''', (name, pwd, email))
    conn.commit()

def setResetKey():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('')

def changePassword(name, newPass):
    'TODO: Test'
    pwd = utils.encrypt(newPass)
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT into USERS(password) values (%s)
        where username = %s ''', (pwd, name));
    conn.commit()
