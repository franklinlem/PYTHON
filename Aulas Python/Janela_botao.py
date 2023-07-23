from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime


def clicked():
    time = strftime('Data: %d %b, %Y.\nHora: %H:%M:%S\n', localtime())
    showinfo(message=time)


root = Tk()
button = Button(root, text='CLIQUE', command=clicked)
button.pack()
root.mainloop()
