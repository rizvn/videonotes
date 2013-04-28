from bottle import route, post, get, request, redirect
import bottle
import re
import urlparse
import app.db_mysql as db
from app.settings import view, getUser

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
                    notes=db.getNotes(vid_pk, getUser()))

@route('/')
@route('/library')
def library():
    return view("library.html", videos = db.getAllVideos())

@post('/note')
def addNote():
    result = db.addNote(request.forms.get('vid_id'),
                                request.forms.get('time'),
                                request.forms.get('text'),
                                getUser())
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
    return view("auth/login.html")

@post('/login')
def auth():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if db.authUser(username, password):
        ses = bottle.request.environ.get('beaker.session')
        ses['user'] = username
        return redirect('/library')
    else:
        return view("auth/login.html", error="Invalid login details")

@get('/logout')
def logout():
    ses = bottle.request.environ.get('beaker.session')
    ses.delete()
    bottle.redirect("/login")


@get('/register')
def registerForm():
    return view('auth/register.html')

@post('/register')
def register():
    return view('auth/register.html', error='User name exists')
