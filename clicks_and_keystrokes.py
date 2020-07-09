import ctypes
import time

user32 = ctypes.windll.user32

keystrokes = 0
mouse_clicks = 0
double_clicks = 0

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

while True:
    print(get_key_press(),mouse_clicks, keystrokes)
    time.sleep(10)
