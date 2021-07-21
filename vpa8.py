import Ui
import cv2
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import datetime
import mymodule2
import search
import face_recognize as fr
import weather as wr
import threading

stare = True
vidCont = True
vidDisplay = True

def displayStare():

    cap = cv2.VideoCapture('videos/stare.mp4')
    cap2 = cv2.VideoCapture('videos/talk.mp4')
    global stare
    global vidCont
    global vidDisplay
    stare2 = stare
    
    minute = datetime.today().minute
    minute2 = minute
    if(cap.isOpened()==False or cap2.isOpened()==False):
        print("Error opening video stream or file")

    while(cap.isOpened() and cap2.isOpened() and vidCont and minute2-minute<2):

        if(vidDisplay) :
            if(stare==True):
                ret,frame = cap.read()
                if ret==True:
                    cv2.imshow('Frame',frame)

                    if cv2.waitKey(25) & 0xFF==ord('q'):
                        break
                else:
                    cap = cv2.VideoCapture('videos/stare.mp4')
            else:
                ret,frame = cap2.read()
                if ret==True:
                    cv2.imshow('Frame',frame)

                    if cv2.waitKey(25) & 0xFF==ord('q'):
                        break
                else:
                    cap2 = cv2.VideoCapture('videos/talk.mp4')

        minute2 = datetime.today().minute

    #print(cap.isOpened(),cap2.isOpened())
    cap.release()
    cap2.release()
    #print(minute,minute2)
    cv2.destroyAllWindows()

class myThread(threading.Thread):

    def run(self):
        displayStare()

thread1 = myThread()

rec = sr.Recognizer()
text = ""

def playSpeech(sound):

    global stare
    stare = False
    playsound(sound,True)
    stare = True


def startThread():
    try:
        thread1.start()
    except:
        print("Unable to open thread")


active = 0
while text!="stop":

    with sr.Microphone() as source:

        print("Speak something")
        
        audio = rec.listen(source)
        text = rec.recognize_google(audio)
        print("You said",text)
        text = text.lower()

        try:

            if (active==0 and (("g" in text) or ("ji" in text)) and ("46" in text) and ("sleep" not in text)):
                active = 1
                hour = datetime.today().hour
                
                if(hour>3 and hour<12):
                    playSpeech("./audios/gm.mp3")
                elif(hour>11 and hour<17):
                    playSpeech("./audios/ga.mp3")
                else:
                    playSpeech("./audios/ge.mp3")

                fr.identify()
                startThread()
                #weather = wr.weather("Deoghar")
                #sp = gTTS(text="Its "+weather[3]+" in Deoghar")
                #sp.save("./audios/weather.mp3")
                #playSpeech("./audios/weather.mp3")


            elif (active==1):
                if(text!="stop"):
                    decision = mymodule2.process(text)
                    if(decision=="disease"):
                        vidDisplay = False
                        Ui.diseasePredict();
                        vidDisplay = True

                    elif(decision!="searchOnGoogle"):
                        playSpeech(decision)
                    else:
                        search.searchOnGoogle(text)
                        playSpeech("./audios/gSays.mp3")
                else:
                    vidCont = False
        except:
            print("Oopsss. Something went wrong")

thread1.join()
#cap.release()
#cap2.release()
#cv2.destroyAllWindows()
