from gtts import gTTS
from playsound import playsound

text = "Enter the symptoms"
speech = gTTS(text=text)
speech.save("enterDisease.mp3")
playsound("enterDisease.mp3",True)
