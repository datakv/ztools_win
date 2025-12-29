import sys
import os
import time
import datetime
from typing import Optional, Tuple
import argparse


import pyautogui

# Initialize controllers
from pynput import mouse, keyboard
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Configuration
DEFAULT_IMAGES = ["image.png", "image2.png"]
CHECK_INTERVAL = 0.8  # seconds


# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接图片文件路径（假设图片名为 image.jpg）
# image_path = os.path.join(script_dir, 'image.jpg')

def find_image(pyautogui, images: list) -> Optional:
    """Search for images on screen, return first match."""
    for img in images:
        tmpImg = image_path = os.path.join(script_dir, img)
        try:
            location = pyautogui.locateOnScreen(tmpImg, confidence=0.9)  # Added confidence parameter
            if location:
                return location
        except pyautogui.ImageNotFoundException:
            continue
    return None


def click_location(mouse_controller, location, button='left') -> None:
    """Click at the center of a location while preserving original mouse position."""
    original_position = mouse_controller.position
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2
    
    mouse_controller.position = (center_x, center_y)
    time.sleep(0.1)
    mouse_controller.click(mouse.Button.left if button == 'left' else mouse.Button.right)
    mouse_controller.position = original_position
    time.sleep(0.1)


def main():
    """Main execution loop."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Monitor and click on specified images")
    parser.add_argument("images", nargs="*", default=DEFAULT_IMAGES, 
                       help="Image file paths to search for (default: image.png image2.png)")
    parser.add_argument("--interval", type=float, default=CHECK_INTERVAL,
                       help=f"Check interval in seconds (default: {CHECK_INTERVAL})")
    parser.add_argument("--no-loop", action="store_true",
                       help="Run once instead of looping")
    
    args = parser.parse_args()
    
    print(f"Starting image monitor with images: {args.images}")
    print("Press Ctrl+C to exit")
    
    
    try:
        while True:
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Searching for {args.images}")
            
            location = find_image(pyautogui, args.images)
            
            if location:
                print(f"Found at: top={location.top}, left={location.left}")
                click_location(mouse_controller, location)
                print("Clicked!")
            
            if args.no_loop:
                break
                
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()