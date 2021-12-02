import enum
from typing import Any, Callable
from flask_socketio import emit
from random import choice

from .timer import TimerThread
from .words import get_variant


class StateEnum(enum.Enum):
    WAIT_FOR_START = 0
    GUESSING = 2


MIN_PLAYERS_FOR_START = 2
GAME_TIME = 120


class GameState:
    def __init__(self, clear_func: Callable):
        self.users = dict()
        self.users_finished = []
        self.state = StateEnum.WAIT_FOR_START
        self.word = ""
        self.drawer = ""
        self.clear = clear_func

    def dispatch(self, action: str, data: Any = None):
        if action == 'START_GAME':
            self.users_finished = []
            self.clear()
            sid = choice(list(self.users.keys()))
            self.word = get_variant()
            self.drawer = sid
            self.state = StateEnum.GUESSING
            emit('state_changed', 'RELOAD', broadcast=True)
            emit('state_changed', self.state.name, broadcast=True)
            emit('set_drawer', self.users[sid], broadcast=True)
            emit('set_word', self.word, to=sid)
        elif action == 'PLAYER_LEFT':
            if len(self.users) < MIN_PLAYERS_FOR_START:
                self.state = StateEnum.WAIT_FOR_START
                emit('state_changed', self.state.name, broadcast=True)
        elif action == 'DRAWER_LEFT':
            if len(self.users) < MIN_PLAYERS_FOR_START:
                self.state = StateEnum.WAIT_FOR_START
                emit('state_changed', self.state.name, broadcast=True)
            else:
                self.dispatch('START_GAME')
        elif action == 'GUESSED_WAITING_ENDED':
            if len(self.users) >= MIN_PLAYERS_FOR_START:
                self.dispatch('START_GAME')
            else:
                self.state = StateEnum.WAIT_FOR_START
                emit('state_changed', self.state.name, broadcast=True)
        elif action == 'PLAYER_GUESSED':
            if len(self.users) - 1 == len(self.users_finished):
                self.dispatch('START_GAME')
        return self.state

    def connect(self, sid: str, name: str):
        self.users[sid] = name
        if len(self.users) >= MIN_PLAYERS_FOR_START:
            self.dispatch('START_GAME')

    def disconnect(self, sid: str):
        if sid in self.users:
            self.users.pop(sid)
        self.dispatch('PLAYER_LEFT')

    def chat(self, sid: str, message: str):
        if sid in self.users_finished or self.drawer == sid:
            return True
        if self.state == StateEnum.GUESSING and message == self.word.strip():
            self.users_finished.append(sid)
            emit('user_completed', self.word)
            self.dispatch('PLAYER_GUESSED')
            return True
        return False
