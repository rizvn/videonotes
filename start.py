from beaker.middleware import SessionMiddleware
from app import vn, auth
import bottle
import os

#Beaker session middleware
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.auto' : True,
    'session.data_dir': 'cache'
}
app = bottle.default_app()
app = SessionMiddleware(app, session_opts)
#port = int(os.environ.get("PORT", 5000))

bottle.run(host='0.0.0.0', port=8080, app=app)


