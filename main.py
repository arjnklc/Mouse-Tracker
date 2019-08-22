import pkg_resources  #Don't delete this line!

from MouseTracker import MouseTracker

from Trayer import Trayer
from util import *


if __name__ == "__main__":

    add_to_startup()
    create_log_file()
    tracker = MouseTracker()
    t = Trayer(tracker)
    t.start()
