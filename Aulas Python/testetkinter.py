from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SAIR", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="OLÁ", command=self.ola)
        self.hi_there.pack(side=LEFT)

    def ola(self):
        print("OLÁ GENTE!")


root = Tk()
app = App(root)
root.mainloop()
