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
    
#--------------- Vidoes-------------------------------------------------
def getAllVideos():
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos')
        return cursor.fetchall()
    
def getVideo(pk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos where pk=?', (pk, ))
        return cursor.fetchone()

#--------------- Notes -------------------------------------------------
def getNotesForVideo(vid_fk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=?', (vid_fk,))
        return cursor.fetchall()

#--------------- Users -------------------------------------------------