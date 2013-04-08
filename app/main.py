from bottle import route, post, get, run, hook, jinja2_view as view, \
            jinja2_template as template, static_file, request
import sqlite3
import app.db as db



def loggedInCheck(fn):
    def wrap():
        print "Performing logged in check"
        return fn()
    return wrap


@hook('before_request')
def login():
    print 'Running login code before request'

@route('/play/<vid_pk>')
def player(vid_pk):
    return template('player.html',
                    video=db.getVideo(vid_pk),
                    notes=db.getNotesForVideo(vid_pk))


@route('/')
def index():
    return template('player.html',
                    video = db.getVideo(1),
                    notes = [{'text' : 'Hello world', 'time': '100'}])

@route('/library')
def library():
    return template("library.html")

@post('/note')
def addNote():
    result = db.addNote(request.forms.get('vid_id'),
                                request.forms.get('time'),
                                request.forms.get('text'),
                                'riz')
    result['ack'] = 1
    return result;

@get('/note/<id:int>/delete')
def deleteNote(id):
    db.deleteNote(id)
    return {'ack': 1}

@post('/note/<id:int>/update')
def updateNote(id):
    db.updateNote(id, request.forms.get('time'), request.forms.get('text'))
    return {'ack': 1}

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root="./static/")
