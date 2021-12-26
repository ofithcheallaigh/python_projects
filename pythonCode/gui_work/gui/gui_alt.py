# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:28:47 2021

@author: Seán

Tutorial: https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
"""

from tkinter import Tk, Label, Button, StringVar
from tkinter import messagebox
from tkinter import *

class MyFirstGUI:
    LABEL_TEXT = ["Why do I keep typing text as test?"]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master,textvariable=self.label_text)
        self.label.bind("<Button-1>",self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.close_window)
        self.close_button.pack()

    # Simple function to show greeting button works
    def greet(self):
        print("Greetings!")
        
    # Function to close the window using the Close button - function will generated
    # a send message to confirm action
    def close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
my_gui = MyFirstGUI(root)
root.protocol("WM_DELETE_WINDOW")       # Used for closing window with the x intop left corner
root.mainloop()
