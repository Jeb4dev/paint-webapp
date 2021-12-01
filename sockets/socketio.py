from uuid import uuid4
from typing import List

from flask import request, session
from flask_socketio import SocketIO, emit

from .path import Point

socketio = SocketIO(logger=True, cors_allowed_origins="*", async_mode="eventlet")

users = dict()
path: List[Point] = []


@socketio.on('connect')
def on_connect():
    if 'name' not in session:
        return False
    name = session['name']

    if name in users:
        name = session['name'] + '-' + str(uuid4()).split('-')[-1]
        session['name'] = name

    users[name] = request.sid
    on_get_paths()


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
