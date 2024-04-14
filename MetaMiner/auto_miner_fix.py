import pyautogui as pag


def userClick(x, y, clicks=1, interval=1):
    pag.moveTo(x, y)
    pag.sleep(0.5)
    pag.click(clicks=clicks, interval=interval)
    pag.sleep(0.5)



def fix():
    pos = pag.locateOnScreen("red_pane.png", region=(714, 324, 490, 166), grayscale=True)
    userClick(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
    userClick(100, 100)
    pag.sleep(0.5)

while True:
    while True:
        try:
            fix()
        except:
            break
    pag.sleep(1)