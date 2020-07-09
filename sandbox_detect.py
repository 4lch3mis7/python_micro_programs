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
    # print(f"It's been {elapsed} milliseconds since the last input event.")
    # print(f"system is running since {run_time} milliseconds.")

    return elapsed

def get_key_press():

    global mouse_clicks
    global keystrokes

    # Iterate over the range of valid input keys
    for i in range(0, 0xff):  # FF = 00000000000000000000000011111111 i.e. 0xFF represents a 32-bit integer

        # We check whether the key has been pressed
        if user32.GetAsyncKeyState(i):

            # 0x1 is the code for a left mouse-click
            if i == 0x1:  # 0x1 is the virtual key code for a left mouse-button click
                mouse_clicks +=1
                return time.time()  # taking timestamp for timing calculations later on
            elif i > 32 and i < 127:  # check if there are ASCII keypresses on the keyboard
                keystrokes +=1

    return None

def detect_sandbox():

    global mouse_clicks
    global keystrokes

    # we randomized the threshold with each run, but you can of course set your own
    max_keystrokes = random.randint(10,25)
    max_mouse_clicks = random.randint(5,25)
    double_clicks = 0
    max_double_clicks = 10
    double_click_threshold = 0.250  # in seconds
    first_double_click = None

    average_mousetime = 0
    max_input_threshold = 30000  # in milliseconds

    previous_timestamp = None
    detection_complete = False

    last_input = get_last_input()

    # if we hit our threshold let's bail out
    if last_input >= max_input_threshold:
        sys.exit(0)

    while not detection_complete:

        keypress_time = get_key_press()

        # if user is giving inputs
        if keypress_time is not None and previous_timestamp is not None:

            # calculate the time between double clicks
            elapsed = keypress_time - previous_timestamp
            

            # the user double clicked
            if elapsed <= double_click_threshold:
                double_clicks += 1

                if first_double_click is None:

                    # grab the the timestamp of the first double click
                    first_double_click = time.time()

                else:

                    #6
                    if double_clicks == max_double_clicks:

                        #7
                        if keypress_time - first_double_click <= (max_double_clicks * double_click_threshold):
                            sys.exit(0)
                        # sys.exit(0)

            # We are happy there's enough user input
            #8
            if keystrokes >= max_keystrokes and double_clicks >= max_double_clicks >= max_mouse_clicks:

                return

            previous_timestamp = keypress_time

        elif keypress_time is not None:
            previous_timestamp = keypress_time
            #print(previous_timestamp)


detect_sandbox()
print("We are okay")








