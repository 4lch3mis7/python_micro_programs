import ctypes
import random
import time
import sys

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

keystrokes = 0
mouse_clicks = 0
double_clicks = 0

# we define LASTINPUTINFO structure that will hold the timestamp (in milliseconds) of when the last input event was detected on the system.
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("dwTime", ctypes.c_ulong)
                ]

def get_last_input():

    # we initialize the cbSize variable to the size of the structure before making the call
    struct_lastinputinfo = LASTINPUTINFO()
    struct_lastinputinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)

    # get last input registered
    user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))
    # now determine how long the machine has been running
    run_time = kernel32.GetTickCount()

    elapsed = run_time - struct_lastinputinfo.dwTime

    # print "[*] It's been %d milliseconds since the last input event."%elapsed  --> in python2
    print(f"It's been {elapsed} milliseconds since the last input event.")
    print(f"system is running since {run_time} milliseconds.")

    return elapsed


# TEST CODE
while True:
    get_last_input()
    time.sleep(1)














