import pygame
from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("Digital Clock")
root.iconbitmap(r'clock1.ico')

def dclock():
    string = strftime("%D:%M:%Y")
    string = strftime("%H:%M:%S %p")
    
    label.config(text = string)
    label.after(1000, dclock)

label = Label(root,font =("Anton-Regular.ttf",50), background = 'grey' , foreground = 'cyan')
label.pack(anchor = 'center')

dclock()

mainloop()