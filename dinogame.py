

import pyautogui
import time
import keyboard

x=801
y=245
#R=83 G=83 B=83 

while 1:
    if pyautogui.pixel(805,209)==(83,83,83):
        pyautogui.keyDown('down')
        time.sleep(0.01)
        pyautogui.keyUp('down')
    if pyautogui.pixel(x,y)!=(255,255,255):
        pyautogui.keyDown('space')
        time.sleep(0.01)
        pyautogui.keyUp('space')
    if keyboard.is_pressed('esc')==True:
        break
    
    
    
    
    