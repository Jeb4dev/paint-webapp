from flask_socketio import SocketIO

socketio = SocketIO(logger=True)


@socketio.on('connect')
def on_connect():
    pass
