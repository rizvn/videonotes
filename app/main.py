from bottle import route, post, get, run, hook, jinja2_view as view, \
            jinja2_template as template, static_file, request, redirect
from threading import local
import sqlite3
import bottle
import app.db as db
import re
import urlparse

req = local()

def loggedInCheck(fn):
    def wrap():
        print "Performing logged in check"
        return fn()
    return wrap

def view(*args, **kwargs):
    #add user name
    kwargs['user'] = req.session['user']
    #render template
    return template(*args, **kwargs)


@hook('before_request')
def login():
    ses = bottle.request.environ.get('beaker.session')
    excludes = ['/login', '/static/']
    for exclude in excludes:
        if exclude in bottle.request.url: return

    if 'user' not in ses:
        redirect('/login')
    else:
        req.session = ses

@route('/play/<vid_pk>')
def player(vid_pk):
    vid = db.getVideo(vid_pk);
    print vid
    youtube_video = 'youtube.com' in vid['url']
    
    if youtube_video:
        params = urlparse.urlparse(vid['url'])[4]
        match = re.match(r"(?P<yt_id>v=(\d|\w)*)", params)
        vid['url'] = match.group('yt_id')[2:]
    
    return view('player.html',
                    video=vid,
                    youtube_video=youtube_video,
                    notes=db.getNotesForVideo(vid_pk))


@route('/')
def index():
    return view('player.html',
                    video = db.getVideo(1),
                    notes = [{'text' : 'Hello world', 'time': '100'}])

@route('/library')
def library():
    return view("library.html", videos = db.getAllVideos())

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

@get('/login')
def login():
    return template("login.html")

@post('/login')
def auth():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if db.authUser(username, password):
        ses = bottle.request.environ.get('beaker.session')
        ses['user'] = username
        return redirect('/library')
    else:
        return template("login.html", error="Invalid login details")

@get('/logout')
def logout():
    ses = bottle.request.environ.get('beaker.session')
    ses.delete()
    redirect("/login");

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root="./static/")
