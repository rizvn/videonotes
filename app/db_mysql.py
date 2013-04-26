import MySQLdb as db
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

#--------------- Notes -------------------------------------------------
def getNotesForVideo(vid_fk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=%s', (vid_fk,))
        return fetchall(cursor)

def getNotes(video_fk, username):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=? and user=?', (video_fk, username))
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
        SET text=?, time=?
        WHERE pk= ?
        ''', (text, time, note_pk))
    conn.commit()

def isAuthor(note_pk, user):
    with Cursor() as cursor:
        cursor.execute('SELECT COUNT(*) from notes where pk=%s and user=%s', (note_pk, user))
        return True if cursor.fetchone()[0] == 1 else False


#--------------- Users -------------------------------------------------
def getUserByName(name):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM users where name=%s', (name,))
        return cursor.fetchone()

def authUser(name, password):
    with Cursor() as cursor:
        cursor.execute("""
            SELECT * FROM users
            WHERE name=%s
            AND password=%s
            """, (name, password))
        return cursor.fetchone()