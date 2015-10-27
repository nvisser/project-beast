__author__ = 'Brumes'

from tkinter import *
from tkinter.messagebox import showinfo

global window, infotekst
window = Tk()
window.configure(background='#FFE917')


def laatschermzien(api):
    toptext=Label(window, text='Welkom bij de NS \n Selecteer een optie')
    toptext.place(x=450, y=150)
    toptext.config(background='#FFE917', foreground='#006', font='Arial 32 bold')
    utrecht = api.zoek('Utrecht Centraal')
    groningen = api.zoek('Groningen')
    Amsterdam = api.zoek('Amsterdam Centraal')
    Rotterdam = api.zoek('Rotterdam Centraal')
    Leiden = api.zoek('Leiden Centraal')
    Schiphol = api.zoek('Schiphol')
    Eindhoven = api.zoek('Eindhoven')
    Amersfoort = api.zoek('Amersfoort')
    Arnhem = api.zoek('Arnhem')
    Houten = api.zoek('Houten')

    button1 = Button(window, text='Utrecht Centraal', command=lambda: zettekstneer(utrecht))

    button1.grid(row=0, column=0, sticky=E, padx=5, pady=5)
    button2 = Button(window, text='Groningen', command=lambda: zettekstneer(groningen))
    button2.grid(row=0, column=1, sticky=E, padx=5, pady=5)
    button3 = Button(window, text='Amsterdam Centraal', command=lambda: zettekstneer(Amsterdam))
    button3.grid(row=0, column=2, sticky=E, padx=5, pady=5)
    button4 = Button(window, text='Rotterdam Centraal', command=lambda: zettekstneer(Rotterdam))
    button4.grid(row=0, column=3, sticky=E, padx=5, pady=5)
    button5 = Button(window, text='Leiden Centraal', command=lambda: zettekstneer(Leiden))
    button5.grid(row=0, column=4, sticky=E, padx=5, pady=5)
    button6 = Button(window, text='Schiphol', command=lambda: zettekstneer(Schiphol))
    button6.grid(row=1, column=0, sticky=E, padx=5, pady=5)
    button7 = Button(window, text='Eindhoven', command=lambda: zettekstneer(Eindhoven))
    button7.grid(row=1, column=1, sticky=E, padx=5, pady=5)
    button8 = Button(window, text='Amersfoort', command=lambda: zettekstneer(Amersfoort))
    button8.grid(row=1, column=2, sticky=E, padx=5, pady=5)
    button9 = Button(window, text='Arnhem', command=lambda: zettekstneer(Arnhem))
    button9.grid(row=1, column=3, sticky=E, padx=5, pady=5)
    button10 = Button(window, text='Houten', command=lambda: zettekstneer(Houten))
    button10.grid(row=1, column=4, sticky=E, padx=5, pady=5)

    window.mainloop()


def zettekstneer(data):
    infotekst = data
    # TODO: label tekst vervangen
    showinfo(title='Vertrektijden', message=infotekst)
