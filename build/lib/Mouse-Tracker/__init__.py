
from pynput.mouse import Listener

import time
from infi.systray import SysTrayIcon


def get_window_name():
    return "sa"
    #return GetWindowText(GetForegroundWindow())


def write_to_file(content, filename="logs"):
    file = open(filename, "a")
    file.write(content+"\n")
    file.close()

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
"""
class Trayer():

    def __init__(self, mouse_tracker):
        self.mouse_tracker = mouse_tracker
        self.activated = True
        self.menu_options = (("Deactivate", None, self.button),)
        self.systray = SysTrayIcon("icon.ico", "Example tray icon", self.menu_options)
        self.mouse_tracker.start_listening()

    def button(self, systray):

        if self.activated:
            print("bitirdim")
            self.mouse_tracker.stop_listening()
        else:
            print("basladim")
            self.mouse_tracker.start_listening()

        self.activated = not self.activated


    # TODO
    def update_menu(self):
        if self.activated:
            self.menu_options = (("Dectivate", None, self.deactivate),)
        else:
            self.menu_options = (("Activate", None, self.activate),)

        self.stop()
        self.start()

    def start(self):
        self.systray.start()

    def stop(self):
        self.systray.shutdown()

"""

print("hello")

