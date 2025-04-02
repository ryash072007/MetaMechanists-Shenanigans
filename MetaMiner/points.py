import pyautogui

fix_points_to_check = [
    (752, 351),
    (800, 349),
    (848, 350),
    (914, 348),
    (960, 350),
    (1022, 348),
    (1065, 348),
    (1126, 348),
    (1172, 346),
    (746, 410),
    (801, 403),
    (857, 404),
    (908, 403),
    (963, 402),
    (1015, 405),
    (1066, 402),
    (1125, 402),
    (1176, 404),
    (742, 458),
    (805, 460),
    (861, 457),
    (907, 456),
    (963, 454),
    (1009, 456),
    (1066, 456),
    (1124, 460),
    (1179, 459),
]

default_pos = (100,100)

def fix_colors():
    for x, y in fix_points_to_check:
        try:
            # Get the RGB color of the pixel at position (x, y)
            pixel_color = pyautogui.pixel(x, y)
            # print(f"Position ({x}, {y}): RGB{pixel_color}")
            if pixel_color == (144, 104, 104):
                print(f"Fixing miner at position ({x}, {y})")
                pyautogui.click(x, y)
        except Exception as e:
            print(f"Could not get color at position ({x}, {y})")
            print(f"Error: {e}")


if __name__ == "__main__":
    pyautogui.moveTo(default_pos)
    # Add a small delay to give you time to switch windows if needed
    print("Starting in 3 seconds...")
    pyautogui.sleep(3)
    fix_colors()
    pyautogui.moveTo(default_pos)
