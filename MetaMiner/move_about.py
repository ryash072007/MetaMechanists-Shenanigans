import pyautogui
import time

switch_left = (799,566)
switch_right = (1125,567)

default_pos = (100,100)

def move_to_third():
    pyautogui.moveTo(switch_right)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(switch_right)
    pyautogui.click()
    print("Moved to 3rd menu")

def move_to_first():
    pyautogui.moveTo(switch_left)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(switch_left)
    pyautogui.click()
    print("Moved to 1st menu")


if __name__ == "__main__":
    pyautogui.moveTo(default_pos)
    # Add a small delay to give you time to switch windows if needed
    print("Starting in 3 seconds...")
    pyautogui.sleep(3)
    move_to_third()
    pyautogui.moveTo(default_pos)
    pyautogui.sleep(1)
    move_to_first()
    pyautogui.moveTo(default_pos)