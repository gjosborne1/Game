from time import sleep
from os import get_terminal_size

def clear():
    print("\033c", end="")

def terminal_height():
    try:
        get_terminal_size()
    except OSError:
        return 3
    else:
        return get_terminal_size().lines-1

def load(revolutions=2):
    remaining = revolutions
    while remaining>0:
        clear()
        print("/", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("|", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("\\", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("—", end="\n"*terminal_height())
        sleep(.2)
        remaining-=.5
    clear()