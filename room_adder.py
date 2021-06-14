
from pynput.keyboard import Key, Controller
import pyperclip
import time
import easygui
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
easygui.msgbox('                               SELECT LIST',ok_button="Click here to select the file")
selectlist=filedialog.askopenfilename()
mylist=open(selectlist,"r")
fd=list()
for line in mylist:
    fd.append(line.strip())
starter=easygui.msgbox('Peopple will be automatically added 10 seconds after you select start. Select the text box after clicking ok')
time.sleep(10)
paste = "xdotool key ctrl+v"
enter= "xdotool key Return"
for i in fd:
    pyperclip.copy(i)
    keyboard=Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
