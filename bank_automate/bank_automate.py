# Log me into my bank account
# because their website doesn't let me copy-paste my account number.

import os
import time

def shellCommand(cmd):
    os.system(cmd)


def typeText(text):
    shellCommand('ydotool type "' + text + '"')


def pressKeys(keys):
    shellCommand('ydotool key ' + keys)


bank_website = 'https://'


def loginToBank(password):

    # Opens incognito tab in Brave Browser
    shellCommand("brave-browser --no-sandbox --incognito {URL}".format(
        URL=bank_website))

    time.sleep(1)

    # Enter Account number
    typeText("")

    time.sleep(0.5)

    # Press TAB twice to focus on "Continue"
    pressKeys("15:1 15:0")
    pressKeys("15:1 15:0")

    # Press ENTER
    pressKeys("28:1 28:0")

    # Enter Password
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


# password = input("Enter your password: ")

loginToBank("PASSWORD")
