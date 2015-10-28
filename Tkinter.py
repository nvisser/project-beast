from tkinter import *
from tkinter.messagebox import showinfo

global window, infotekst
window = Tk()
window.resizable(0,0)
window.wm_title("Team Beast NS Applicatie")
window.configure(background='#FFE917')
window.geometry('{}x{}'.format(1280, 720))
window.protocol('WM_DELETE_WINDOW', lambda: quitwindow())


def laatschermzien(api):
    window.deiconify()
    toptext = Label(window, text='Van welk station wilt u actuele vertrektijden zien?')
    toptext.place(x=240, y=150)
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

    button1 = Button(window, text='Utrecht CS', command=lambda: zettekstneer(utrecht))
    button1.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button1.place(x=250, y=270)
    button2 = Button(window, text='Groningen', command=lambda: zettekstneer(groningen))
    button2.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button2.place(x=250, y=320)
    button3 = Button(window, text='Amsterdam CS', command=lambda: zettekstneer(Amsterdam))
    button3.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button3.place(x=250, y=370)
    button4 = Button(window, text='Rotterdam CS', command=lambda: zettekstneer(Rotterdam))
    button4.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button4.place(x=250, y=420)
    button5 = Button(window, text='Leiden CS', command=lambda: zettekstneer(Leiden))
    button5.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button5.place(x=250, y=470)
    button6 = Button(window, text='Schiphol', command=lambda: zettekstneer(Schiphol))
    button6.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button6.place(x=1030, y=270)
    button7 = Button(window, text='Eindhoven', command=lambda: zettekstneer(Eindhoven))
    button7.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button7.place(x=1030, y=320)
    button8 = Button(window, text='Amersfoort', command=lambda: zettekstneer(Amersfoort))
    button8.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button8.place(x=1030, y=370)
    button9 = Button(window, text='Arnhem', command=lambda: zettekstneer(Arnhem))
    button9.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button9.place(x=1030, y=420)
    button10 = Button(window, text='Houten', command=lambda: zettekstneer(Houten))
    button10.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    button10.place(x=1030, y=470)

    quit = Button(window, text='Terug naar hoofdmenu', command = quitwindow)
    quit.config(width=16, height=1, background='#003082', foreground='white', font='Arial 14 bold')
    quit.place(x=1030, y=570)
    window.mainloop()

def quitwindow():
    window.withdraw()


def zettekstneer(data):

    infotekst = data
    # TODO: label tekst vervangen
    infolabel = Label(window, text = infotekst)
    infolabel.configure(text = infotekst)
    infolabel.config(width=50, height=15, background='#FFE917', foreground='#003082', font='Arial 12 bold')
    infolabel.place(x=475, y=270)