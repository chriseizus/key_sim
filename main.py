from pystray import MenuItem as item
import pystray
from PIL import Image
import time

from pynput.keyboard import Key, Controller

pause = False


def exit():
    icon.visible = False
    icon.stop()

def startswitch():
    global pause
    pause = False

def pauseswitch():
    global pause
    pause = True

def action(icon):
    icon.visible = True
    keyboard = Controller()
    
    i = 0
    while icon.visible:
        # Some payload code
        print(pause)
        if pause != True:
            keyboard.press(Key.ctrl)
            keyboard.release(Key.ctrl)
        
        time.sleep(10)    


image = Image.open("icon.png")
menu = (
    item('Start', startswitch),
    item('Pause', pauseswitch), 
    item('Exit', exit)
)
icon = pystray.Icon("name", image, "title", menu)
icon.run(action)