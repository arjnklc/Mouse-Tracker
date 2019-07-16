from infi.systray import SysTrayIcon


class Trayer():

    def __init__(self, mouse_tracker):
        self.mouse_tracker = mouse_tracker
        self.activated = True
        self.menu_options = (("Activate", None, self.activate), ("Deactivate", None, self.deactivate),)
        self.systray = SysTrayIcon("bogazici.ico", "BUICS Security Lab", self.menu_options)
        self.mouse_tracker.start_listening()

    def start(self):
        self.systray.start()

    def activate(self, systray):
        self.activated = True
        self.mouse_tracker.start_listening()
        print("Activated")

    def deactivate(self, systray):
        self.activated = False
        self.mouse_tracker.stop_listening()
        print("Deactivated")







