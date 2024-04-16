import pyautogui as pag
import subprocess

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

for x in range(200):
    try:
        fix()
    except:
        pass
    pag.sleep(1)


subprocess.Popen(["python", "miner_2.py"])
exit()