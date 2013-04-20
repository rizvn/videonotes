from bottle import route, post, get, run, hook, jinja2_view as view, \
            jinja2_template as template, static_file, request
import sqlite3
import bottle
import app.db as db
import re
import urlparse



def loggedInCheck(fn):
    def wrap():
        print "Performing logged in check"
        return fn()
    return wrap


@hook('before_request')
def login():
    ses = bottle.request.environ.get('beaker.session')
    if 'user' not in ses:
        print('Setting up user')
        ses['user'] = 'anonymous'
    else:
        print ('Existing user', ses['user'])

    print 'Running login code before request'

@route('/play/<vid_pk>')
def player(vid_pk):
    vid = db.getVideo(vid_pk);
    print vid
    youtube_video = 'youtube.com' in vid['url']
    
    if youtube_video:
        params = urlparse.urlparse(vid['url'])[4]
        match = re.match(r"(?P<yt_id>v=(\d|\w)*)", params)
        vid['url'] = match.group('yt_id')[2:]
    
    return template('player.html',
                    video=vid,
                    youtube_video=youtube_video,
                    notes=db.getNotesForVideo(vid_pk))


@route('/')
def index():
    return template('player.html',
                    video = db.getVideo(1),
                    notes = [{'text' : 'Hello world', 'time': '100'}])

@route('/library')
def library():
    return template("library.html", videos = db.getAllVideos())

@post('/note')
def addNote():
    result = db.addNote(request.forms.get('vid_id'),
                                request.forms.get('time'),
                                request.forms.get('text'),
                                'riz')
    result['ack'] = 1
    return result

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
