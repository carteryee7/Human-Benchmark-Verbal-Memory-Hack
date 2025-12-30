from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X: 1170 Y:  785 RGB: (153, 158, 231)
#X: 1355 Y:  785 RGB: (171, 174, 233)
#X: 1550 Y:  785 RGB: (170, 173, 233)
#X: 1804 Y:  785 RGB: (  0,   0,   0)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1170, 785)[0] == 0:
        click(1170, 785)
    if pyautogui.pixel(1355, 785)[0] == 0:
        click(1355, 785)
    if pyautogui.pixel(1550, 785)[0] == 0:
        click(1550, 785)
    if pyautogui.pixel(1804, 785)[0] == 0:
        click(1804, 785)
