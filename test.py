from tkinter import *

from pystray import MenuItem as item
from PIL import Image, ImageTk

from res import * #here is my base64 encoded icon. Variable icon_base64.
from base64 import b64decode

import pystray
import base64
import time



def run_icon():
    #image = Image.open("icon.ico") #uncomment this to use a standard image, isntead of base64.
    title="Tray title"
    image = Image.open("icon.png") #comment this if using standard way of image
    menu = (item('test1', lambda: show_notification(),default = True), item('Exit', lambda: exit()))
    global icon
    icon = pystray.Icon("name", image, title, menu)
    icon.run()
    
def show_notification(text):
    icon.notify(text,"My test notification sub title")

def show():

    print("exit")

run_icon()
time.sleep(3)
show_notification("test")