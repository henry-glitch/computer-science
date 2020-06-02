
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("say Anything :")
    audio = r.listen(source)
    try:
        text = (audio)
        print("You said : "+  audio)
    except:
        print("Sorry could not recognize what you said")