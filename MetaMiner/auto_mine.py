import time
import pyautogui
import threading
import sys
from move_about import move_to_first, move_to_third
from collect_coin import collect
from points import fix_colors

# Global flag to control the script
running = True

# Override PyAutoGUI's click function to add delay after each click
original_click = pyautogui.click
def click_with_delay(*args, **kwargs):
    # Double-click to ensure registration
    original_click(*args, **kwargs)
    time.sleep(0.05)  # Small delay between clicks
    original_click(*args, **kwargs)
    time.sleep(0.1)  # Shorter delay after double-click
pyautogui.click = click_with_delay

# Function to monitor keyboard input in a separate thread
def keyboard_monitor():
    global running
    print("Press Ctrl+C in this console window to stop the script")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False
        print("\nStop signal received. Stopping script gracefully...")

def run_mining_cycle():
    """
    Runs the complete mining automation cycle:
    - Collects coins every second
    - Every 10 collections, fixes miners by checking colors
    """
    global running
    
    print("Starting automated mining management...")
    print("Non-fullscreen Minecraft 1.21.1 mode")
    
    # Add a delay to switch to the game window
    print("Starting in 3 seconds...")
    pyautogui.sleep(3)
    
    cycle_count = 0
    
    try:
        while running:
            # Start in the first menu
            if not running: break
            move_to_first()
            
            # Collect coins every second for 10 collections
            for i in range(10):
                if not running:
                    break
                print(f"Collection {i+1}/10")
                collect()
                pyautogui.moveTo(100, 100)  # Move to default position
                time.sleep(1)
            
            if not running:
                break
                
            # After 10 collections, go to third menu and fix colors
            cycle_count += 1
            print(f"\nCompleted cycle {cycle_count}, now fixing miners...")
            move_to_third()
            pyautogui.sleep(0.5)  # Short wait
            fix_colors()
            
            # Move back to default position
            pyautogui.moveTo(100, 100)
            print("Miners fixed, starting next cycle...\n")
            
    except Exception as e:
        print(f"\nError occurred: {e}")
        running = False
    finally:
        print("Mining automation ended")

if __name__ == "__main__":
    # Start keyboard monitoring thread
    keyboard_thread = threading.Thread(target=keyboard_monitor)
    keyboard_thread.daemon = True
    keyboard_thread.start()
    
    try:
        run_mining_cycle()
    except Exception as e:
        print(f"Error in main thread: {e}")
    finally:
        print("Script finished")