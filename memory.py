import pyautogui
import pytesseract
from PIL import Image
import mss
import mss.tools
import time
import win32api, win32con
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# *******************************************************************
# NOTE: You may need to specify the path to the tesseract executable
# if it's not in your system's PATH.
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# *******************************************************************

def get_text_from_region(region):
    """
    Captures a screen region and performs OCR to extract text.

    Args:
        region (tuple): A 4-integer tuple of (left, top, width, height)
                        defining the area to capture.
    Returns:
        str: The extracted text.
    """
    with mss.mss() as sct:
        # Capture the specified region
        sct_img = sct.grab(region)
        # Convert to a PIL Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
        return text.strip()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Define the region to monitor (example: top-left 300x300 pixel area)
# Format: (left, top, width, height)
# You will need to adjust these coordinates for your specific use case.
monitor_region = {"top": 353, "left": 1016, "width": 500, "height": 100}

print(f"Monitoring screen region: {monitor_region}")
print("Press Ctrl+C to exit.")

seen = set()

try:
    while True:
        detected_word = get_text_from_region(monitor_region)
        if detected_word:
            if detected_word in seen:
                print(f"Already Seen: {detected_word}")
                click(1209, 480)
            else:
                seen.add(detected_word)
                print(f"New Word: {detected_word}")
                click(1346, 480)

        if keyboard.is_pressed('q') == True:
            raise KeyboardInterrupt
        
        time.sleep(.05) # Wait a second before the next capture to prevent high CPU usage
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")
