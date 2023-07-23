from tkinter import Tk, PhotoImage, Label

root = Tk()
imagem = PhotoImage(file='pc.gif').subsample(5)
janela = Label(master=root, image=imagem, width=270, height=190)
janela.pack()
root.mainloop()
