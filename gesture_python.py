# gesture control python program for controlling certain functions in windows pc
# Code by BalaAppu
# Website: www.electronicshub.org

import serial                                      # add Serial library for serial communication
import pyautogui
import psutil, win32process, win32gui, time
name = '';

def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    print(psutil.Process(pid[-1]).name())
    return psutil.Process(pid[-1]).name()
# add pyautogui library for programmatically controlling the mouse and keyboard.

Arduino_Serial = serial.Serial('com4',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
 
while 1:
    incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
    print incoming_data                            # print the incoming Serial data
    name = active_window_process_name() 

    if 'next' in incoming_data:                # if incoming data is 'next'
        if(name == 'ApplicationFrameHost.exe'):
            print 'space'
            pyautogui.press('space')
        else:
            pyautogui.hotkey('ctrl', 'pgdn')           # perform "ctrl+pgdn" operation which moves to the next tab

    
        
    if 'previous' in incoming_data:                # if incoming data is 'previous'
        if(name == 'ApplicationFrameHost.exe'):
            print 'space'
            pyautogui.press('space')
        else:
            pyautogui.hotkey('ctrl', 'pgup')                          # perform "ctrl+pgup" operation which moves to the previous tab

    if 'down' in incoming_data:                    # if incoming data is 'down'
        #pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.scroll(-100) 
         
    if 'up' in incoming_data:                      # if incoming data is 'up'
        #pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        pyautogui.scroll(100)
        
    if 'change' in incoming_data:                  # if incoming data is 'change'
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
    incoming_data = "";                            # clears the data
