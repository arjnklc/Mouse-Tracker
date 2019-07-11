from infi.systray import SysTrayIcon


class Trayer():

    def __init__(self, mouse_tracker):
        self.mouse_tracker = mouse_tracker
        self.activated = True
        self.menu_options = (("Activate", None, self.activate), ("Deactivate", None, self.deactivate),)
        self.systray = SysTrayIcon("icon.ico", "Example tray icon", self.menu_options)
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

"""
    # TODO
    def update_menu(self):
        if self.activated:
            self.menu_options = (("Dectivate", None, self.button),)
        else:
            self.menu_options = (("Activate", None, self.button),)

        self.systray.update()




    def stop(self):

        self.systray.shutdown()
"""





