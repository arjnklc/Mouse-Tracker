from pynput.mouse import Listener
import time

from util import *


class MouseTracker:

    def __init__(self):
        self.track = True
        self.started_timestamp = time.time()

    def on_move(self, x, y):
        timestamp = time.time() - self.started_timestamp
        s = "{0:.4f} {1} {2} Movement {3}".format(timestamp, x, y, get_window_name())
        write_to_file(s)

    def on_click(self, x, y, button, pressed):
        timestamp = time.time() - self.started_timestamp
        s = "{0:.4f} {1} {2}".format(timestamp, x, y)
        if pressed:  # press or release check
            if str(button) == "Button.right":
                s += " Pressed right "
            elif str(button) == "Button.left":
                s += " Pressed left "
        else:
            if str(button) == "Button.right":
                s += " Released right "
            elif str(button) == "Button.left":
                s += " Released left "

        s += get_window_name()

        write_to_file(s)

    # TODO
    def on_scroll(self, x, y, dx, dy):
        print("scroll")
        timestamp = time.time() - self.started_timestamp
        s = "{0:.4f} Scrolled {1}".format(timestamp, (x, y))
        write_to_file(s)

    def start_listening(self):
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click)
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()
