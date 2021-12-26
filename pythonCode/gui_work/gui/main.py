# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:45:17 2021

@author: Seán
"""

from tkinter import *
from tkinter import ttk # python bindings for themed widgets

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

# Code below tells Tk that the frame should expand to fill 
# any extra space if the window is resized
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Creates the Entry widget and puts it on screen
feet = StringVar()
feet_entry = ttk.Entry(mainframe,width=7,textvariable=feet)
feet_entry.grid(column=2,row=1,sticky=(N,E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2,row=2,sticky=(N,E))
ttk.Button(mainframe,text="Calculate",command=calculate).grid(column=3,row=2,sticky=W)
ttk.Label(mainframe,text="feet").grid(column=3,row=1,sticky=W)
ttk.Label(mainframe,text="is equivalent to").grid(column=1,row=2,sticky=E)
ttk.Label(mainframe,text="meters").grid(column=3,row=2,sticky=W)

# Adding some polish
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
feet_entry.focus()
root.bind("<Return>",calculate)

root.mainloop()


