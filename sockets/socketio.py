from flask import request
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, cors_allowed_origins="*", async_mode="eventlet")


@socketio.on('connect')
def on_connect():
    print(request.args)
