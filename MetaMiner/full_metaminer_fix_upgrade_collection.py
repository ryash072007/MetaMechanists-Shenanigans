import pyautogui as pag
from datetime import datetime



def userClick(x, y, clicks=1, interval=1):
    pag.moveTo(x, y)
    pag.sleep(0.5)
    pag.click(clicks=clicks, interval=interval)


def update():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") + " => "

    print(dt_string + "Starting Coin collecting procedure")
    print("Proceeding to Page 1")
    userClick(802, 584, 2)  # Page 1

    print("Collecting coins")
    userClick(963, 569)  # Collect MetaCoin

    print("Proceeding to Page 2")
    userClick(1122, 565)  # Page 2

    print("Trying to upgrade")
    userClick(958, 415)  # Try upgrade

    print("Proceeding to Page 3")
    userClick(1122, 565)  # Fixer Page


def fix():
    pos = pag.locateOnScreen("red_pane.png", region=(714, 324, 500, 175))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") + " => "
    print(dt_string + "Red Pane Detected: Attempting to fix it")
    userClick(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
    userClick(100, 100)


start_time = datetime.now()

while True:
    if (datetime.now() - start_time).seconds > 2400:  # Do this every 40 minutes
        start_time = datetime.now()
        update()

    try:
        fix()
    except:
        pass

