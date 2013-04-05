from bottle import route, post, run, hook, jinja2_view as view, \
            jinja2_template as template, static_file
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
    return template('player.html', video=db.getVideo(vid_pk))


@route('/')
def index():
    return template('player.html',
                    video = db.getVideo(1),
                    notes = [{'content' : 'Hello world', 'timeCode': '100'}])

@route('/library')
def library():
    return template("library.html")

@post('/note')
def addNote():
    return "<div>123</div>"

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root="./static/")
