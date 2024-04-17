import pyautogui as pag
from datetime import datetime


def userClick(x, y, clicks=1, interval=1):
    pag.moveTo(x, y)
    pag.sleep(0.5)
    pag.click(clicks=clicks, interval=interval)
    pag.sleep(0.5)


def fix():
    pos = pag.locateOnScreen("red_pane.png", region=(714, 324, 490, 166))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") + " => "
    print(dt_string + "Red Pane Detected: Attempting to fix it")
    userClick(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
    userClick(100, 100)
    pag.sleep(0.5)


while True:
    try:
        fix()
        print("Attempting To Fix!")
    except:
        pass
    pag.sleep(1)
