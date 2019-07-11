#from win32gui import GetWindowText, GetForegroundWindow


def get_window_name():
    return "sa"
    #return GetWindowText(GetForegroundWindow())


def write_to_file(content, filename="logs"):
    file = open(filename, "a") 
    file.write(content+"\n") 
    file.close()
