__author__ = 'Brumes'

from tkinter import *


def laatschermzien(api):
    window = Tk()
    label = Label(window, text='Van welk station wilt u de vertrektijden weten?')
    label.pack()
    data = api.verkrijg_utrecht()
    button = Button(window, text='Utrecht', command=lambda: zettekstneer(data))
    button.pack()

    window.mainloop()

def zettekstneer(data):
    print(data)
