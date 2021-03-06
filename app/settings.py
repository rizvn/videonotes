settings = {
    #sqlite config
    'db_path': 'db/videonotes.db',

    #Mysql config
    'host': 'localhost',
    'port': 3306,
    'user': 'riz',
    'passwd': 'pass',
    'db': 'videonotes'
}

import socket
hostname = socket.gethostname()



#jinja2 templates
from app.utils import sec_to_time
from jinja2 import Environment, FileSystemLoader
jinja_env = Environment(loader=FileSystemLoader('views'))
jinja_env.filters['sec_to_time'] = sec_to_time

import bottle
def view(*args, **kwargs):
    #add user name
    kwargs['user'] = getUser()
    return jinja_env.get_template(args[0]).render(**kwargs)

def getUser():
    ses = bottle.request.environ.get('beaker.session')
    return ses['user'] if 'user' in ses else None

@bottle.route('/static/<filepath:path>')
def serve_static(filepath):
    return bottle.static_file(filepath, root="./static/")

@bottle.hook('before_request')
def checkLoggedIn():
    excludes = ['/login', '/static/', '/register', '/resetPassword']
    for exclude in excludes:
        if exclude in bottle.request.url: return
    if not getUser():
        bottle.redirect('/login')
