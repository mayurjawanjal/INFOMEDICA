import search
from gtts import gTTS
import weather as wr
from playsound import playsound
import speech_recognition as sr
from datetime import datetime
rec = sr.Recognizer()

Q0 = {"your","name"}
Q1 = {"who","created","creator","creators"}
Q2 = {"single","relation","relationship","marital","status"}
Q3 = {"president","india"}
Q4 = {"primeminister","prime","minister","india"}
Q5 = {"captain","cricket","india","indian"}
Q6 = {"your","hobby","hobbies"}
Q7 = {"what","today","todays","today's","weather"}
Q8 = {"what","what's","date","day"}
Q9 = {"what","what's","time"}
Q10 = {"disease","prediction"}


Q = [Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]

def corresMonth(mon):
    if mon==1:
        return "January"
    elif mon==2:
        return "February"
    elif mon==3:
        return "March"
    elif mon==4:
        return "April"
    elif mon==5:
        return "May"
    elif mon==6:
        return "June"
    elif mon==7:
        return "July"
    elif mon==8:
        return "August"
    elif mon==9:
        return "September"
    elif mon==10:
        return "October"
    elif mon==11:
        return "November"
    elif mon==12:
        return "December"

def process(text):
    ques = text
    text = text.split()
    for i in range(len(Q)):
        res = Q[i].intersection(text)
        if len(res)>1:
 #           print(Q[i])
            if i==0:
                return "./audios/name.mp3"
            elif i==1:
                return "./audios/creatorNames.mp3"
            elif i==2:
                return "./audios/maritalStatus.mp3"
            elif i==3:
                #search.searchOnGoogle(ques)
                return "./audios/pOI.mp3"
            elif i==4:
                #search.searchOnGoogle(ques)
                return "./audios/pmOI.mp3"
            elif i==5:
                #search.searchOnGoogle(ques)
                return "./audios/cOI.mp3"
            elif i==6:
                return "./audios/hobby.mp3"
            elif i==7:

                playsound("./audios/loc.mp3",True)
                loc = ''
                with sr.Microphone() as source:
                    audio = rec.listen(source)
                    loc = rec.recognize_google(audio)
                print("You said = ",loc)
                weather = wr.weather(loc)
                print("WEATHER = ",weather)
                if(len(weather)==4):
                    #print("***")
                    sp = gTTS("Its "+str(weather[3])+" in "+loc+" . Temperature is "+str(int(weather[0]))+" degree celsius , atmospheric pressure is "+str(weather[1])+" h p a , and humidity is "+str(weather[2])+" percentage .")
                    #print("****")
                    sp.save("./audios/weather.mp3")
                    #print("*****")
                    return "./audios/weather.mp3"
                else:
                    #print("&&&&&")
                    return "./audios/invalLoc.mp3"
            
            elif i==8:
                sp = gTTS("Its "+str(datetime.today().day)+" "+corresMonth(datetime.today().month)+" "+str(datetime.today().year))
                sp.save("./audios/datetime.mp3")
                return "./audios/datetime.mp3"

            elif i==9:
                sp = gTTS("Its "+str(datetime.today().hour)+" hours, "+str(datetime.today().minute)+" minutes, "+str(datetime.today().second)+" seconds")
                sp.save("./audios/datetime.mp3")
                return "./audios/datetime.mp3"

            elif i==10:
                return "disease"
    else :
        return "searchOnGoogle"

#process("what is your name")
