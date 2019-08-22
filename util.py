import os
import wmi
import psutil, win32process, win32gui
import shutil

c = wmi.WMI()


def get_window_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    try:
        return psutil.Process(pid[-1]).name() #pid[-1] is the most likely to survive last longer
    except:
        return ""


def write_to_file(content, filename="logs"):
    try:
        file = open(filename, "a")
        file.write(content+"\n")
        file.close()
    except Exception as e:
        print(getattr(e, 'message', repr(e)))


def log(content):
    user = str(os.getlogin())
    user.strip()
    path = 'C:/Users/' + user + '/MouseData/logs.txt'
    write_to_file(content, path)

def create_log_file():
    user = str(os.getlogin())
    user.strip()
    dir = 'C:/Users/' + user + '/MouseData'
    if not os.path.exists(dir):
        os.makedirs(dir)


def add_to_startup():
    user = str(os.getlogin())
    user.strip()
    src = os.getcwd() + "/tracker.exe"
    dest = 'C:/Users/' + user + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
    try:
        shutil.copy2(src, dest)
    except Exception as e:
        print(getattr(e, 'message', repr(e)))

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False