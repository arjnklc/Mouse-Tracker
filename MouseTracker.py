from pynput.mouse import Listener
import time
import threading
import sched, time

from util import *


class MouseTracker:

    def __init__(self):
        self.track = True
        self.started_timestamp = time.time()
        self.listener = None
        self.reactivate()


    def on_move(self, x, y):
        timestamp = time.time()
        s = "Movement {0:.4f} {1} {2} None Move {3}".format(timestamp, x, y, get_window_name())
        log(s)

    def on_click(self, x, y, button, pressed):
        timestamp = time.time()
        s = "Click {0:.4f} {1} {2}".format(timestamp, x, y)
        if pressed:  # press or release check
            if str(button) == "Button.right":
                s += " Right Pressed "
            elif str(button) == "Button.left":
                s += " Left Pressed "
        else:
            if str(button) == "Button.right":
                s += " Right Released "
            elif str(button) == "Button.left":
                s += " Left Released "

        s += get_window_name()
        log(s)


    def start_listening(self):
        try:
            self.stop_listening()
        except:			
            pass	 
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click)
            
        self.listener.start()



    def stop_listening(self):
        try:
            self.listener.stop()
        except:
            pass

    def reactivate(self):
        rt = RepeatedTimer(1800, self.start_listening) # 3600 saniye = 1 saat
