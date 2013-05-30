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

bottle.run(host='0.0.0.0', port=5000, app=app, reloader=True)
