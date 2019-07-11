from infi.systray import SysTrayIcon


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
    def activate(self, systray):
        self.activated = True
        self.mouse_tracker.start_listening()
        self.update_menu()

        print("Activated")

    def deactivate(self, systray):
        self.activated = False
        self.mouse_tracker.stop_listening()
        self.update_menu()
        print("Deactivated")
"""
