import pyautogui

collect_pos = (961,569)

default_pos = (100,100)

def collect():
    pyautogui.moveTo(collect_pos)
    pyautogui.click()
    print("Collecting coins...")

if __name__ == "__main__":
    # Add a small delay to give you time to switch windows if needed
    print("Starting in 3 seconds...")
    pyautogui.sleep(3)
    pyautogui.moveTo(default_pos)
    collect()
    pyautogui.moveTo(default_pos)