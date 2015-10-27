__author__ = 'Brumes'

from tkinter import *

window = Tk()
window.geometry('{}x{}'.format(1280, 720))

window.configure(background='yellow')
mmbutton = Button(window, text="Placeholder")
mmbutton.place(x=200, y=200)
mmbutton.config(width=20, height=10)

mmbutton = Button(window, text="Placeholder")
mmbutton.place(x=400, y=200)
mmbutton.config(width=20, height=10)

mmbutton = Button(window, text="Placeholder")
mmbutton.place(x=600, y=200)
mmbutton.config(width=20, height=10)

mmbutton = Button(window, text="Placeholder")
mmbutton.place(x=800, y=200)
mmbutton.config(width=20, height=10)

mmbutton = Button(window, text="Placeholder")
mmbutton.place(x=1000, y=200)
mmbutton.config(width=20, height=10)

window.mainloop()
