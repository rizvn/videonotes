from bottle import route, run, jinja2_view as view, \
            jinja2_template as template, static_file
import sqlite3



def loggedInCheck(fn):
    def wrap():
        print "Performing logged in check"
        return fn()
    return wrap

@route('/')
@loggedInCheck
def index():
    return template('index.html',
                    vid_title="Paradox of Choice",
                    vid_author="Barry Schwartz",
                    vid_location="/static/testVideos/paradox_of_choice.mp4",
                    notes = [{'content' : 'Hello world', 'timeCode': '100'}])

@route('/library')
def library():
    return template("library.html",
            videos= [{title: 'Hello World'}, {title: 'bye world'}]        
            )


@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root="./static/")
