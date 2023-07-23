from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='pc.gif').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
texto = Label(master=root, text='TESTANDO TEXTO NA JANELA!', font=('courier', 18,))
texto.pack(side=BOTTOM)
root.mainloop()
