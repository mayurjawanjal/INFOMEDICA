import speech_recognition as sr

rec = sr.Recognizer()
text = ""

#print("Speak something...")
with sr.Microphone() as source:
    print("Speak something...")
    audio = rec.listen(source)
    text = rec.recognize_google(audio)
    print(text)
    print(type(text))
