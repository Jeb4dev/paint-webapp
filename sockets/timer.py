from threading import Thread
from typing import Callable
from time import sleep


class TimerThread(Thread):
    def __init__(self, seconds: int, callback: Callable, *args, **kwargs):
        self.default_seconds = seconds
        self.seconds = seconds
        self.callback = callback
        self.paused = False
        self.__stop = False
        super().__init__(*args, **kwargs)

    def resume(self):
        self.paused = False

    def pause(self):
        self.paused = True

    def reset(self):
        self.seconds = self.default_seconds
        self.paused = False

    def stop(self):
        self.__stop = True

    def run(self):
        while self.seconds >= 0:
            if self.__stop:
                break
            sleep(1)
            if not self.paused:
                self.seconds -= 1
        if not self.__stop:
            self.callback()
