from bottle import route, run
from bottle import jinja2_view as view, jinja2_template as template
from Configuration import Configuration
from bottle import static_file

conf = Configuration()

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
                    vid_location="/static/testVideos/paradox_of_choice.mp4")

@route('/library')
def library():
    return template("library.html")


@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root="./static/")





run(host='localhost', port=8080, debug=True)
