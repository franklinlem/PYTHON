import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'pt-br')
    engine.say(text)
    engine.runAndWait()

text_to_speech("Olá, mundo!")