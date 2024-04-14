import pyautogui as pag

time_since_collected = 0
cycles_since_fix = 0


def userClick(x, y, clicks=1, interval=1):
    global time_since_collected
    pag.moveTo(x, y)
    pag.sleep(0.5)
    pag.click(clicks=clicks, interval=interval)
    time_since_collected += 1


def update():
    global time_since_collected
    time_since_collected = 0

    print("Starting Coin collecting procedure")
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
    global cycles_since_fix
    pos = pag.locateOnScreen("red_pane.png", region=(714, 324, 490, 166))
    userClick(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
    userClick(100, 100)
    pag.sleep(0.5)
    cycles_since_fix += 1


while True:
    if cycles_since_fix >= 5:
        cycles_since_fix = 0
        pag.hotkey("alt", "tab")
        pag.sleep(2)
        time_since_collected += 2
        pag.hotkey("alt", "tab")
        userClick(100, 100)

    if time_since_collected >= 1200:  # Do this every 20 minutes
        update()

    try:
        fix()
    except:
        pass

    time_since_collected += 1
    pag.sleep(1)
