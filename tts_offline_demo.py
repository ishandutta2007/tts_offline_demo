import pyttsx3
with open ("data.txt", "r", encoding="utf8") as myfile:
    text = myfile.read().splitlines()

engine = pyttsx3.init('sapi5')
# engine.setProperty('rate',145)
engine.say(text)
engine.runAndWait()
