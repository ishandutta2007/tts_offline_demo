import pyttsx3
with open ("data.txt", "r") as myfile:
    text = myfile.read().splitlines()
engine = pyttsx3.init('sapi5')
engine.say(text)
engine.runAndWait()
