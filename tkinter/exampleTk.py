# coding: utf-8
from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text='Click Me')
button.pack()
ttk.Label(root, text='Hello, Tkinter').pack()
root.mainloop()
