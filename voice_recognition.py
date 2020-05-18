def callback(recognizer,audio): 
    try: 
        Speech= recognizer.recognize_google(audio) 
        ReactToSpeech(Speech)
   except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
   except sr.RequestError as e: 
        print("Could not request results from service; {0}".format(e)) 
def ReactToSpeech(Speech): 
   if "mirror on the wall" in Speech: 
        Say("Who is the fairest of them all") # From last tutorial
def StopListening(): 
   stop_listening(wait_for_stop=False) 