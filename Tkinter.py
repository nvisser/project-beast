__author__ = 'Brumes'

from tkinter import *

global window
window = Tk()


def laatschermzien(api):
    label = Label(window, text='Van welk station wilt u de vertrektijden weten?')
    label.pack()
    data = api.verkrijg_utrecht()
    button = Button(window, text='Utrecht', command=lambda: zettekstneer(data))
    button.pack()

    window.mainloop()


def zettekstneer(data):
    label = Label(window, text=data)
    label.pack()
