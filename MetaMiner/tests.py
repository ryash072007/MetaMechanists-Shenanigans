import pyautogui
import keyboard

def print_cursor_position(_):
    x, y = pyautogui.position()
    print(f"({x},{y}),")

# Monitor for Enter key press
keyboard.on_press_key('enter', print_cursor_position)

print("Press Enter to see cursor position (Ctrl+C to exit)")
keyboard.wait('ctrl+c')  # Keep program running until Ctrl+C is pressed