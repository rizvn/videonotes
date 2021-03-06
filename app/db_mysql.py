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

class CommitCursor():
    def __enter__(self):
        self.conn = getConnection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.conn.commit()
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

def getVideos(tags=None, createdBy=None, count=None):
    with Cursor() as cursor:
        #what to project
        project = " COUNT(*) " if count else " * "
        query = "SELECT %s FROM VIDEOS " % project

        #where clauses
        tagsq = None if not tags else "tags = '%s' " % (tags, )
        createdByq = None if not createdBy else "createdBy = '%s' " % (createdBy, )

        query += utils.joinWheres([tagsq, createdByq])
        cursor.execute(query)
        return fetchall(cursor)

def addVideo(title, url, createBy, shared, tags):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
      INSERT INTO VIDEOS(title, url, createdBy, shared, tags)
      VALUES (%s, %s, %s, %s, %s )
    ''', (title, url, createBy, shared, tags))
    conn.commit()
    videoPk = cursor.lastrowid
    return {'id': videoPk}


def getVideo(pk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos where pk=%s', (pk, ))
        return fetchone(cursor)

#--------------- Notes -------------------------------------------------
def getNotesForVideo(vid_fk):
    with Cursor()  as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s', (vid_fk,))
        return fetchall(cursor)

def getNotes(video_fk, username):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s and user=%s', (video_fk, username))
        return fetchall(cursor)

def getUserAndSharedNotes(video_fk, user):
    with Cursor() as cursor:
        cursor.execute('''
        select * from notes
        where vid_fk =%s
        and (user=%s or share=1)
        ''', (video_fk, user))
        return fetchall(cursor)

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
    with CommitCursor() as cursor:
        cursor.execute('DELETE FROM notes where pk = %s', (note_pk,))

def updateNote(note_pk, time, text):
    with CommitCursor() as cursor:
        cursor.execute('''
            UPDATE notes
            SET text=%s, time=%s
            WHERE pk= %s
            ''', (text, time, note_pk))


def updateShare(note_pk, share):
    with CommitCursor() as cursor:
        cursor.execute('''
        UPDATE notes
        SET share = %s
        WHERE pk = %s''', (share, note_pk))

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
