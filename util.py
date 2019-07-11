from win32gui import GetWindowText, GetForegroundWindow

import wmi
import psutil, win32process, win32gui


c = wmi.WMI()

def get_window_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    try:
        return psutil.Process(pid[-1]).name() #pid[-1] is the most likely to survive last longer
    except:
        return ""

def get_window_name2():
    return GetWindowText(GetForegroundWindow())


def write_to_file(content, filename="logs"):
    try:
        file = open(filename, "a")
        file.write(content+"\n")
        file.close()
    except:
        pass


# TODO
def add_to_startup():
    pass