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
port = int(os.environ.get("PORT", 8080))

import socket
hostname = socket.gethostname()
#if on heroku host name will not contain rizvan
if 'Rizvan' in hostname:
    bottle.run(host='0.0.0.0', port=port, app=app)


