import os
import time
from evdev import InputDevice, categorize, ecodes

# macro_kbd = InputDevice('/dev/input/by-id/usb-SIGMACHIP_USB_Keyboard-event-kbd')
macro_kbd = InputDevice('/dev/input/event2')

# Get keycodes for your keyboard.
# print(macro_kbd.capabilities(verbose=True))

macro_kbd.grab()

# Get Key IDs
# less /usr/include/linux/input-event-codes.h | cat

# Implement Python Switch Case Statement using Dictionary

# Using ydotool instad of xdotool for wayland compatibility
# https://github.com/ReimuNotMoe/ydotool


def typeText(text):
    os.system('ydotool type "' + text + '"')


def pressKeys(keys):
    os.system('ydotool key ' + keys)


def enterPassword():
    # This is an insecure way of handling passwords!
    # TODO: Make use of .env files?
    password = ''
    typeText(password)


def fun(keyPressed):
    # Switch-case like function.
    # Usable only on Python version 3.10 and above.
    match keyPressed:
        case 0:
            return 0

# Actual Functions Implemented


def Key_1():
    # Ctrl + F1
    # Switch to Desktop 1
    return pressKeys("29:1 59:1 59:0 29:0")


def Key_2():
    # Ctrl + F2
    # Switch to Desktop 2
    return pressKeys("29:1 60:1 60:0 29:0")


def Key_3():
    # Ctrl + F3
    # Switch to Desktop 3
    return pressKeys("29:1 61:1 61:0 29:0")


def Key_4():
    # Ctrl + F4
    # Switch to Desktop 4
    return pressKeys("29:1 62:1 62:0 29:0")


def PressEnter():
    # Press ENTER
    return pressKeys("28:1 28:0")

def ToggleMute():
    # Press MUTE Function Button
    return pressKeys("113:1 113:0")

def VolumeDown():
    # Press VOL UP Function Button
    return pressKeys("114:1 114:0")


def VolumeUp():
    # VOL UP Function Button
    return pressKeys("115:1 115:0")


def Undo():
    # Ctrl + Z
    # Undo
    return pressKeys("29:1 44:1 44:0 29:0")


def DrawOn():
    # Press
    # Left Meta + Left Shift
    return pressKeys("125:1 42:1")


def DrawOff():
    # Release
    # Left Meta + Left Shift
    return pressKeys("125:0 42:0")


def OpenGlobalSearch():
    # "Activities" on GNOME, KRunner on KDE, ULauncher, etc.
    # Left Meta + Left Alt
    return pressKeys("56:1 57:1 56:0 57:0")

def OpenBankPortal():
    # Gets the bank password from user
    # and then logs into bank website automatically
    bank_website = 'https://netbanking.hdfcbank.com/netbanking'

    def loginToBank(password):

        # Opens incognito tab in Brave Browser
        os.system(f"brave-browser --incognito {bank_website}")

        time.sleep(1)

        # Enter Account number
        typeText('170248590')

        time.sleep(0.5)

        # Press TAB twice to focus on "Continue"
        pressKeys("15:1 15:0")
        pressKeys("15:1 15:0")

        # Press ENTER
        pressKeys("28:1 28:0")

        # Enter Password
        # typeText('170248590')
        time.sleep(1)

        # Press TAB thrice to focus on "This is my Secure ID"
        # and then press SPACE to check the box
        pressKeys("15:1 15:0")
        pressKeys("15:1 15:0")
        pressKeys("15:1 15:0")
        pressKeys("57:1 57:0")

        # Press SHIFT + TAB thrice to get focus back on
        # the password field, to enter the password
        pressKeys("42:1 15:1 15:0 42:0")
        pressKeys("42:1 15:1 15:0 42:0")
        pressKeys("42:1 15:1 15:0 42:0")

        # Enter PASSWORD TEMPORARILY
        # And press ENTER

        typeText(password)
        pressKeys("28:1 28:0")
    password = 'input("Enter your password: ")'

    return loginToBank(password)

def default():
    # When key is not an assigned macro
    # return typeText("No macro assigned...")
    return os.system("echo 'No macro assigned...'")

def YSSAltar():
    # Super + L_Shift + A
    pressKeys("125:1 42:1 30:1 30:0 42:0 125:0")



macros = {

    0: default,
    "KEY_ESC": default,  # Escape
    "KEY_1": Key_1,  # 1
    "KEY_2": Key_2,  # 2
    "KEY_3": Key_3,  # 3
    "KEY_4": Key_4,  # 4
    "KEY_5": default,  # 5
    "KEY_6": default,  # 6
    "KEY_7": default,  # 7
    "KEY_8": default,  # 8
    "KEY_9": default,  # 9
    "KEY_0": default,  # 0
    "KEY_MINUS": default,  # Minus, Hyphen
    "KEY_EQUAL": default,  # Equal, Plus
    "KEY_BACKSPACE": default,  # Backspace
    "KEY_TAB": default,  # Tab
    "KEY_Q": default,  # Q
    "KEY_W": default,  # W
    "KEY_E": default,  # E
    "KEY_R": default,  # R
    "KEY_T": default,  # T
    "KEY_Y": default,  # Y
    "KEY_U": default,  # U
    "KEY_I": default,  # I
    "KEY_O": default,  # O
    "KEY_P": default,  # P
    "KEY_LEFTBRACE": DrawOn,  # {[
    "KEY_RIGHTBRACE": DrawOff,  # }]
    "KEY_KPENTER": PressEnter,  # ENTER
    "KEY_LEFTCTRL": default,  # LEFT_CTRL
    "KEY_A": default,  # A
    "KEY_S": default,  # S
    "KEY_D": default,  # D
    "KEY_F": default,  # F
    "KEY_G": default,  # G
    "KEY_H": default,  # H
    "KEY_J": default,  # J
    "KEY_K": default,  # K
    "KEY_L": default,  # L
    # When Numlock is ON, KEY_L becomes KEY_KP3
    "KEY_KP3": ToggleMute,  # L
    "KEY_SEMICOLON": default,  # ;
    # When Numlock is ON, KEY_SEMICOLON becomes KEY_KPPLUS
    "KEY_KPPLUS":  VolumeDown,  # ;
    "KEY_APOSTROPHE": VolumeUp,  # '
    "KEY_GRAVE": YSSAltar,  # Tilde or ~
    "KEY_LEFTSHIFT": default,  # LEFT_SHIFT
    "KEY_BACKSLASH": enterPassword,  # BACKSLASH
    "KEY_Z": Undo,  # Z
    "KEY_X": OpenBankPortal,  # X
    "KEY_C": default,  # C
    "KEY_V": default,  # V
    "KEY_B": default,  # B
    "KEY_N": default,  # N
    "KEY_M": default,  # M
    "KEY_COMMA": default,  # ,
    "KEY_DOT": default,  # .
    "KEY_SLASH": default,  # /
    "KEY_RIGHTSHIFT": default,  # RIGHT_SHIFT
    "KEY_KPASTERISK": default,  # *
    "KEY_LEFTALT": default,  # LEFT_ALT
    "KEY_SPACE": OpenGlobalSearch,  # SPACEBAR
    "KEY_CAPSLOCK": default,  # CAPS_LOCK
    "KEY_F1": default,  # F1
    "KEY_F2": default,  # F2
    "KEY_F3": default,  # F3
    "KEY_F4": default,  # F4
    "KEY_F5": default,  # F5
    "KEY_F6": default,  # F6
    "KEY_F7": default,  # F7
    "KEY_F8": default,  # F8
    "KEY_F9": default,  # F9
    "KEY_F10": default,  # F10
    "KEY_F11": default,  # F11
    "KEY_F12": default,  # F12
    "KEY_NUMLOCK": default,  # NUM_LOCK
    "KEY_SCROLLLOCK": default,  # SCROLL_LOCK
    "KEY_RIGHTCTRL": default,  # RIGHT_CTRL
    "KEY_RIGHTALT": default,  # RIGHT_ALT
    "KEY_KPSLASH": default,  # Numpad SLASH
    "KEY_SYSRQ": default,  # SYSRQ
    "KEY_HOME": default,  # HOME
    "KEY_UP": default,  # UP
    "KEY_LEFT": default,  # LEFT
    "KEY_RIGHT": default,  # RIGHT
    "KEY_END": default,  # END
    "KEY_DOWN": default,  # DOWN
    "KEY_PAGEDOWN": default,  # PAGE_DOWN
    "KEY_PAGEUP": default,  # PAGE_UP
    "KEY_INSERT": default,  # INSERT
    "KEY_DELETE": default,  # DELETE
    "KEY_MUTE": default,
    "KEY_VOLUMEUP": default,
    "KEY_VOLUMEDOWN": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": default,
    "KEY_": ''  # LEFT_META
    # 'KEY_UP':  os.system('xdotool type "pspe1004"'),
    # 'KEY_ESC': os.system('echo Hello World'),
}


def execMacro(key_code):
    # every key has a "key_code", which
    # may vary between different keyboards.

    # Use the following in the beginning of the code to find out yours.
    # print (macro_kbd.capabilities(verbose=True))

    return macros.get(key_code, default)()


for event in macro_kbd.read_loop():
    if event.type == ecodes.EV_KEY:
        # print(event)
        key = categorize(event)
        print(f"Press State of {key.keycode} is {key.keystate}")
        if key.keystate == key.key_down:
            print('\n[Key Pressed]', key.keycode)
            execMacro(key.keycode)

            # execMacro(event.keycode)
            #             if key.keycode == 'KEY_ESC':
            #                 os.system('echo Hello World')

            #             if key.keycode == 'KEY_UP':
            #                 os.system('xdotool type "pspe1004"')

            #             # print the pressed key
            #             print(key.keycode)

            # print(execMacro(3))
            # print(execMacro(5))
