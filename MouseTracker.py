from pynput.mouse import Listener
import time

from util import *


class MouseTracker:

    def __init__(self):
        self.track = True
        self.started_timestamp = time.time()


    def on_move(self, x, y):
        timestamp = time.time() - self.started_timestamp
        s = "{0:.4f} {1} {2}".format(timestamp, x, y)
        write_to_file(s)

    def on_click(self, x, y, button, pressed):
        timestamp = time.time() - self.started_timestamp
        s = ""
        if pressed:
            if str(button) == "Button.right":
                s = "{0:.4f} Pressed right".format(timestamp)
            elif str(button) == "Button.left":
                s = "{0:.4f} Pressed left".format(timestamp)

        else:
            s = "{0:.4f} Released".format(timestamp)

        write_to_file(s)

    def start_listening(self):
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click)
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()
