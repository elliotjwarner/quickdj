import tkinter as tk
from tkinter import *
from pygame import mixer
import os
import random

# initialize the pygame mixer
mixer.init(44100)
soundList=[]#stores all sounds in folder
variable=['','','','','','','','','','']

# used to set songs
def setSounds():
    global tempSoundArray
    s=[]
    for i in range(10):
        inputs = "./sounds/"+variable[i].get()
        s.insert(i,mixer.Sound(inputs))
    
    tempSoundArray = s
    
# used to set songs to keys
def on_key(event):
    # detect any normal key press (0..9, A..Z, a..z)
    soundArray = tempSoundArray
    if event.char == event.keysym:
        soundArray[int(event.char)-1].play()

# set random sounds on start
def rand():
    for i in range(10):
        variable[i].set(soundList[random.randint(0,9)])
    setSounds()

# main loop calls GUI and helper functions
def mainloop():

    # initialize sound list from sounds folder
    i=0
    for filename in os.listdir("./sounds"):
        if filename.endswith(".mp3"): 
            soundList.insert(i, filename)
            i += 1

    # create GUI
    root = Tk()

    # create button that changes sounds
    button = Button(root, text="set sounds", command=setSounds, width =25)
    button.pack(side="top")
    button.bind_all('<Key>', on_key)  

    # add dropdowns to GUI
    for i in range(10):
        variable[i] = tk.StringVar(root)#initialize
        opt = OptionMenu(root, variable[i], *soundList)#drop down functionality
        opt.pack(side="left")#structure

    # initialize dropdown with rand sounds
    rand()
    root.mainloop() 

mainloop()