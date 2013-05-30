from beaker.middleware import SessionMiddleware
from app import vn, auth
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

bottle.run(host='localhost', port=8080, app=app, reloader=True)
