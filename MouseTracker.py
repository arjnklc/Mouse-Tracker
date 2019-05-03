from pynput.mouse import Listener
import time


class MouseTracker:

    def __init__(self):
        self.started_timestamp = time.time()

    def on_move(self, x, y):
        timestamp = time.time() - self.started_timestamp
        print("{0:.4f} {1} {2}".format(timestamp, x, y))

    def on_click(self, x, y, button, pressed):
        timestamp = time.time() - self.started_timestamp
        if pressed:
            if str(button) == "Button.right":
                print("{0:.4f} Pressed right".format(timestamp))
            elif str(button) == "Button.left":
                print("{0:.4f} Pressed left".format(timestamp))
        else:
            print("{0:.4f} Released".format(timestamp))

    def listen_forever(self):
        with Listener(on_move=self.on_move, on_click=self.on_click) as listener:
            listener.join()
