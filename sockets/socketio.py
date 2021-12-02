from uuid import uuid4
from typing import List

from flask import request, session
from flask_login import current_user
from flask_socketio import SocketIO, emit

from .path import Point
from .state import GameState

socketio = SocketIO(logger=True, cors_allowed_origins="*", async_mode="eventlet")

users = dict()
path: List[Point] = []
state: GameState


@socketio.on('connect')
def on_connect():
    if 'name' not in session:
        return False

    if current_user.is_authenticated:
        session['name'] = current_user.username

    name = session['name']

    if name in users:
        name = session['name'] + '-' + str(uuid4()).split('-')[-1]
        session['name'] = name

    state.connect(request.sid, name)
    emit('user_connected', name, broadcast=True)
    emit('state_changed', state.state.name)
    on_get_paths()


@socketio.on('disconnect')
def on_disconnect():
    if request.sid in state.users:
        emit('user_left', state.users[request.sid])
    state.disconnect(request.sid)


@socketio.on('add_paths')
def on_get_paths(data: List[Point]):
    emit('add_paths', data, broadcast=True, include_self=False)
    path.extend(data)


@socketio.on('get_paths')
def on_get_paths():
    emit('get_paths', path)


@socketio.on('clear')
def on_clear():
    path.clear()
    emit('clear', broadcast=True)


@socketio.on('undo')
def on_undo():
    global path
    path = path[:-1]
    emit('undo', path[-10:], broadcast=True)


@socketio.on('chat')
def on_chat(message):
    right = state.chat(request.sid, message)
    emit('chat', {
        "username": session['name'],
        "message": message,
        "completed": right
    }, broadcast=True)


state = GameState(on_clear)
