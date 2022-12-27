import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
            
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk ('Playing ' + music)
        pywhatkit.playonyt(music)

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%H:%M %p')
        talk('Son las ' + hora)

    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)

    elif 'chiste' in rec:
        broma = pyjokes.get_joke(language='es', category= 'all')
        talk('Ok   ' + broma ) 
    
    elif 'gracias' in rec:
        talk('Por nada, estoy para ayudarte')

    elif 'estás' in rec:
        talk('Muy bien y tú?')

    else:
        talk("Retry")

while True:
    run()