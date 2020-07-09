def clr_src():
    from os import system, name
    if name == 'nt':
        return system('cls')  # for windows
    else:
       return system('clear')  # for MacOS and Linux
