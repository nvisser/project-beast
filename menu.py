from tkinter import *
from tkinter.messagebox import showinfo
import Tkinter
import api


def popup():
    showinfo(title='Popup', message='This button is useless')

def submenu():
    Tkinter.laatschermzien(api)


window = Tk()
window.wm_title("Team Beast NS Applicatie")
window.configure(background='#FFE917')
window.geometry('{}x{}'.format(1920, 1080))


toptext = Label(window, text='Welkom bij de NS \n Selecteer een optie')
toptext.place(x=450, y=150)
toptext.config(background='#FFE917', foreground='#006', font='Arial 32 bold')

mmbutton = Button(window, text="Kopen \n los kaartje", command=lambda: popup())
mmbutton.place(x=70, y=350)
mmbutton.config(width=20, height=10, background='#003082', foreground='white', font='Arial 14 bold')

mmbutton = Button(window, text="Kopen \n OV-chipkaart", command=lambda: popup())
mmbutton.place(x=370, y=350)
mmbutton.config(width=20, height=10, background='#003082', foreground='white', font='Arial 14 bold')


mmbutton = Button(window, text="Ik wil naar \n het buitenland", command=lambda: popup())
mmbutton.place(x=670, y=350)
mmbutton.config(width=20, height=10, background='#003082', foreground='white', font='Arial 14 bold')


mmbutton = Button(window, text="Actuale \n vertrektijden", command=lambda: submenu())
mmbutton.place(x=970, y=350)
mmbutton.config(width=20, height=10, background='#003082', foreground='white', font='Arial 14 bold')


window.mainloop()
