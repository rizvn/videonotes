import sqlite3

class Cursor():
    def __enter__(self):
        conn = sqlite3.connect('db/videonotes.db')
        self.cursor = conn.cursor()
        return self.cursor
    
    def __exit__(self, type, value, traceback):
        self.cursor.close();
        print "Type: ",type
        print "Value: ", value
        print "Trace: ", traceback
        return not traceback 
    


def getAllVideos():
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM videos')
        return cursor.fetchall()

def getNotesForVideo(vid_fk):
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM notes where vid_fk=?', (vid_fk,))
        return cursor.fetchall()

def addNote(arg1):
    pass

def deleteNote(arg1):
    pass




