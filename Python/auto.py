# ENGLISH

import pyautogui
import time


edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge"
url = "https://docs.google.com/forms/d/e/1FAIpQLSft1MHAijPxvTFy3o9mb_uCCKSkC1rgjjuBHAi1DWydRqnEpQ/viewform"
gmail = "rishikesh.sahyogcollege@gmail.com"
enrollment = "CV195030088"
# ===============================================<< Enter Subject >>==================================================


def tab():
    pyautogui.PAUSE = 1
    pyautogui.press('tab')


def english():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')


def dbms():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')


def dsa():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')


def networking():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')


def java():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')


def webDev():
    tab()
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

# =================================================<< Variables >>===============================================


# ===============================================<< Browser Opening >>============================================


def browserOpening():
    pyautogui.hotkey('winleft', 'd')
    pyautogui.PAUSE = 1
    pyautogui.hotkey('winleft', 'r')
    pyautogui.PAUSE = 1
    pyautogui.typewrite(edge)
    pyautogui.PAUSE = 1
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')
    time.sleep(2)

# =============================================<< Open URL >>==================================================


def openUrl():
    pyautogui.typewrite(url)
    time.sleep(1)
    pyautogui.press("enter")


# =================================================<< Enter Details >>==================================================


def enterDetails():
    time.sleep(10)
    pyautogui.click(472, 558, 1, 1, 'left')
    time.sleep(0.200)
    pyautogui.typewrite(gmail)
    time.sleep(0.200)
    tab()
    time.sleep(0.200)
    pyautogui.press('enter')
    time.sleep(0.200)
    pyautogui.press('r')
    time.sleep(0.200)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(0.200)
    tab()
    pyautogui.typewrite(enrollment)
    tab()
    pyautogui.press('enter')
    pyautogui.press('s')
    pyautogui.press('enter')
    tab()
    pyautogui.press('enter')
    pyautogui.press('b')
    pyautogui.press('enter')


# ==============================================================================================================


def entersub():
    print("Choose Subject")
    print("1. English")
    print("2. DBMS")
    print("3. DSA")
    print("4. Networking")
    print("5. Java")
    print("6. WebDev")
    print("")
    subject = int(input())

    if(subject == 1):

        browserOpening()
        openUrl()
        enterDetails()
        english()

    elif(subject == 2):

        browserOpening()
        openUrl()
        enterDetails()
        dbms()

    elif(subject == 3):

        browserOpening()
        openUrl()
        enterDetails()
        dsa()

    elif(subject == 4):

        browserOpening()
        openUrl()
        enterDetails()
        networking()

    elif(subject == 5):

        browserOpening()
        openUrl()
        enterDetails()
        java()

    elif(subject == 6):

        browserOpening()
        openUrl()
        enterDetails()
        webDev()

    else:
        print("")
        entersub()


entersub()
