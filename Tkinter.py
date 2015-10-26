__author__ = 'Brumes'

from tkinter import *

global window, infotekst
window = Tk()


def laatschermzien(api):
    label = Label(window, text='Van welk station wilt u de vertrektijden weten?')
    label.pack()
    utrecht = api.zoek('Utrecht')
    groningen = api.zoek('Groningen')
    button1 = Button(window, text='Utrecht', command=lambda: zettekstneer(utrecht))
    button1.pack()
    button2 = Button(window, text='Groningen', command=lambda: zettekstneer(groningen))
    button2.pack()

    window.mainloop()


def zettekstneer(data):
    infotekst = data
    # TODO: label tekst vervangen
    label = Label(window, text=infotekst)
    label.pack()
