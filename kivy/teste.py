import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    print("Como funciona essa merda?")

    def build(self):
        return Label(text='Olá FULEIROS!!!')


if __name__ == '__main__':
    MyApp().run()