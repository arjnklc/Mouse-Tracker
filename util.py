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
    except:
        pass


def get_windows_version():
    return "Windows 10"


# TODO
def add_to_startup():
    if get_windows_version() == "Windows 10":
        user = str(os.getlogin())
        user.strip()
        src = os.getcwd() + "/tracker.exe"
        dest = 'C:/Users/' + user + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
        shutil.copy2(src, dest)

    elif get_windows_version() == "Windows 7":
        pass
