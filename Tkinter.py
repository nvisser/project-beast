__author__ = 'Brumes'

from tkinter import *
from tkinter.messagebox import showinfo

global window, infotekst
window = Tk()
window.wm_title("Team Beast NS Applicatie")


def laatschermzien(api):
    label = Label(window, text='Van welk station wilt u de vertrektijden weten?')
    label.pack()
    utrecht = api.zoek('Utrecht Centraal')
    groningen = api.zoek('Groningen')
    Amsterdam = api.zoek('Amsterdam Centraal')
    Rotterdam = api.zoek('Rotterdam Centraal')
    Leiden = api.zoek('Leiden Centraal')
    Schiphol = api.zoek('Schiphol')
    Eindhoven  = api.zoek('Eindhoven')
    Amersfoort  = api.zoek('Amersfoort')
    Arnhem  = api.zoek('Arnhem')
    Houten  = api.zoek('Houten')
    button1 = Button(window, text='Utrecht Centraal', command=lambda: zettekstneer(utrecht))
    button1.pack()
    button2 = Button(window, text='Groningen', command=lambda: zettekstneer(groningen))
    button2.pack()
    button3 = Button(window, text='Amsterdam Centraal', command=lambda: zettekstneer(Amsterdam))
    button3.pack()
    button4 = Button(window, text='Rotterdam Centraal', command=lambda: zettekstneer(Rotterdam))
    button4.pack()
    button5 = Button(window, text='Leiden Centraal', command=lambda: zettekstneer(Leiden))
    button5.pack()
    button6 = Button(window, text='Schiphol', command=lambda: zettekstneer(Schiphol))
    button6.pack()
    button7 = Button(window, text='Eindhoven', command=lambda: zettekstneer(Eindhoven))
    button7.pack()
    button8 = Button(window, text='Amersfoort', command=lambda: zettekstneer(Amersfoort))
    button8.pack()
    button9 = Button(window, text='Arnhem', command=lambda: zettekstneer(Arnhem))
    button9.pack()
    button10 = Button(window, text='Houten', command=lambda: zettekstneer(Houten))
    button10.pack()

    window.mainloop()


def zettekstneer(data):
    infotekst = data
    # TODO: label tekst vervangen
    #label = Label(window, text=infotekst)
    #label.pack()

    showinfo(title='Vertrektijden', message=infotekst)

