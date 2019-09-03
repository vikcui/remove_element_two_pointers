# author : YANG CUI
#   ID   : 27346919

"""
The objective is to create a simple notepad in Python using Tkinter.
This notepad GUI will consist of various menu like file and edit, using
which all functionalities like saving the file, opening a file, editing, cut and paste can be done.
"""

import tkinter

window = tkinter.Tk()

# to rename the title of the window window.title("GUI")

# pack is used to show the object in the window

label = tkinter.Label(window, text="Hello World!").pack()

window.mainloop()
