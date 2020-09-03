import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('COM5',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print (incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.press('space')

    if 'Rewind' in incoming:
        pyautogui.press('left')
        #hotkey('ctrl', 'left')  

    if 'Forward' in incoming:
        pyautogui.press('right')
        #hotkey('ctrl', 'right') 

    if 'Vup' in incoming:
        pyautogui.press('down')
        #hotkey('ctrl', 'down')
        

    if 'Vdown' in incoming:
        pyautogui.press('up')
        #hotkey('ctrl', 'up')
  
    incoming = ""
