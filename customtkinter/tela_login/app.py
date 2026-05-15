from pydoc import text
from tkinter import Button
from turtle import color

import customtkinter as ctk
from eel import show

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if usuario == 'Franklin' and senha == '123456':
        resultado.configure(text='Login correto!', text_color='green')
    else:
        resultado.configure(text='Login incorreto! Nome de Usuario ou senha inválido!', text_color='red')


modo = ctk.set_appearance_mode('dark')
app  = ctk.CTk()
titulo = app.title('Tela de Login')
tamanho = app.geometry('300x300')

label_usuario = ctk.CTkLabel(app, text='Usuario')
label_usuario.pack(pady=10)
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuario')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

botao = ctk.CTkButton(app, text='Login', command=validar_login)
botao.pack(pady=10)

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)


app.mainloop()