__author__ = 'milan'
from tkinter import *

def clicked():
   print('Jij bent ' + lft.get() + ' jaar')

window = Tk()
label = Label(window, text = 'Voer je leeftijd in')
label.pack()

lft = Entry(window)
lft.pack()

button = Button(window,text='Voer in', command=clicked)
button.pack()

window.mainloop()
