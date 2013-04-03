import sqlite3
from app.settings import settings

class Cursor():
    def __enter__(self):
        conn = sqlite3.connect(settings['db_path'])
        self.cursor = conn.cursor()
        return self.cursor
    
    def __exit__(self, type, value, traceback):
        self.cursor.close();
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
        cursor.execute('SELECT * FROM videos where pk=?', (pk, ))
        return fetchone(cursor)

#--------------- Notes -------------------------------------------------
def getNotesForVideo(vid_fk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=?', (vid_fk,))
        return fetchall(cursor)


def addNote(vid_fk, time, text, user):
    conn = sqlite3.connect(settings['db_path'])
    conn.cursor().execute('''
        INSERT INTO notes (vid_fk, time, text, user)
        VALUES (?, ?, ?, ?)
        ''', (vid_fk, time, text, user))
    conn.commit()

def deleteNote(note_pk):
    conn = sqlite3.connect(settings['db_path'])
    conn.cursor().execute('''
        DELETE FROM notes where pk = ?                      
    ''', (note_pk,))
    conn.commit()

#--------------- Users -------------------------------------------------
def getUserByName(name):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM users where name=?', (name,))
        return cursor.fetchone()
    
def authUser(name, password):
    with Cursor() as cursor:
        cursor.execute("""
            SELECT * FROM users
            WHERE name=?
            AND password=?
            """, (name, password))
        return cursor.fetchone()

