from bottle import route, run
from bottle import jinja2_view as view, jinja2_template as template
from Configuration import Configuration

conf = Configuration()

def loggedInCheck(fn):
    def wrap():
        print "Performing logged in check"
        return fn()

    return wrap

@route('/hello')
@loggedInCheck
def hello():
    global conf
    conf.incCount()
    return "Hello world count: {count}".format(count=conf.count)

@route('/dictTest')
def dictTest():
    notes = {}
    notes[10] = "abc"
    notes[9] = "def"
    return notes

@route('/jinjaDemo')
def jinjaDemo():
    return template('test.html', message="Hello world")

'''
@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{name}}, how are you?', name=name)
'''
run(host='localhost', port=8080, debug=True)
