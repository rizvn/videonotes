from app import main
from beaker.middleware import SessionMiddleware

import bottle

#Beaker session middleware
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.auto' : True,
    'session.data_dir': 'cache'
}
app = bottle.default_app()
app = SessionMiddleware(app, session_opts)

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


bottle.run(host='localhost', port=8080, app=app, debug=True, reloader=True)
