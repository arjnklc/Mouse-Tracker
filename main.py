from MouseTracker import MouseTracker
from Trayer import Trayer

from util import *

if __name__ == "__main__":

    print(get_window_name())
    tracker = MouseTracker()
    t = Trayer(tracker)
    t.start()

