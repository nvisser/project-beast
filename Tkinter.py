__author__ = 'Brumes'

from tkinter import *


def laatschermzien(api):
    window = Tk()
    label = Label(window, text='Van welk station wilt u de vertrektijden weten?')
    label.pack()
    button = Button(window, text='Utrecht', command=lambda: api.verkrijg_utrecht())
    button.pack()

    window.mainloop()
