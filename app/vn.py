from bottle import route, post, get, request, response
import re
import json
import urlparse
import app.db_mysql as db
import app
import app.utils as utils
from app.settings import view, getUser


@route('/play/<vid_pk>')
def player(vid_pk):
    vid = db.getVideo(vid_pk);
    youtube_video = 'youtube.com' in vid['url']
    
    if youtube_video:
        params = urlparse.urlparse(vid['url'])[4]
        match = re.match(r"(?P<yt_id>v=(\d|\w)*)", params)
        vid['url'] = match.group('yt_id')[2:]

    notes = db.getNotes(vid_pk, getUser())
    sorted_notes = utils.sortNotes(notes)
    return view('player.html',
                    video=vid,
                    youtube_video=youtube_video,
                    notes=sorted_notes)

@route('/')
@route('/library')
def library():
    tags = request.query.get('tags')
    return view("library.html", videos=db.getVideos(tags=tags), tags=tags)

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
    if db.isAuthor(id, getUser()):
        db.deleteNote(id)
        return {'ack': 1}
    else:
        return {'ack': 0, 'msg':'You do not have permission delete this note'}

@post('/note/<id:int>/update')
def updateNote(id):
    if db.isAuthor(id, getUser()):
        db.updateNote(id, request.forms.get('time'), request.forms.get('text'))
        return {'ack': 1}
    else:
        return {'ack': 0, 'msg':'You do not have permission update this note'}

@post('/note/<id:int>/share')
def shareNote(id):
    if db.isAuthor(id, getUser()):
        db.updateShare(id, 1)
        return {'ack': 1}
    else:
        return {'ack': 0, 'msg':'You do not have permission update this note'}

@post('/note/<id:int>/unshare')
def unShareNote(id):
    if db.isAuthor(id, getUser()):
        db.updateShare(id, 0)
        return {'ack': 1}
    else:
        return {'ack': 0, 'msg':'You do not have permission update this note'}


@get('/notes/<vid_fk:int>')
def getNotes(vid_fk):
    type = request.query.get('type')
    share = request.query.get('share')
    user = getUser();

    if share == '1':
     notes = db.getUserAndSharedNotes(vid_fk, user)
    else:
     notes = db.getNotes(vid_fk, user)

    notes = utils.sortNotes(notes)

    if type=='json':
        response.content_type='application/json'
        return json.dumps(notes, default=app.utils.jsonSerializer)
    else:
        return view("notes.html", notes=notes)

@get("/videos/add")
def addVideoForm():
    return view("add_video_form.html")

@post('/videos/add')
def addVideo():
    title  = request.forms.get('title')
    url    = request.forms.get('url')
    shared = request.forms.get('shared')
    shared = shared if shared is not None else 0

    tags = request.forms.get('tags')
    username = getUser()
    errors = []

    if title is None:
        errors.append("Title required")

    if url is None:
        errors.append("URL required")

    if tags is None:
        errors.append("No tags specified")

    #if no errors create a video entry
        #send ack back

    #else return errors

