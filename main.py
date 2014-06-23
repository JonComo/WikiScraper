__author__ = 'joncomo'

import wikipedia

from tkinter import *


master = Tk()

master.size = (600, 400)

e = Entry(master)
e.pack()

e.focus_set()

longText = StringVar()

label = Label(master=master, textvariable=longText, justify=LEFT, wraplength=600).pack()


def load():
    page = wikipedia.page(title=e.get(), auto_suggest=True)
    longText.set(page.summary)


b = Button(master, text="get", width=20, command=load)
b.pack()

mainloop()