import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import smtplib
import psutil
import pyjokes
import os
import pyautogui
import wolframalpha

engine = pyttsx3.init()
wolframalpha_app_id='7G8JL8-PKLL6HY764'#wolfram aplpha id will go go here


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")#FOR 24 HOURS CLOCK
    speak("THE CURRENT TIME IS")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

#time_()
#date_()
def wishme():
    speak("welcome back shama")
    time_()
    date_()

    #greetings
    hour =datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning shama")
    elif hour>=12 and hour<18:
        speak("Good Afternoon shama")
    elif hour>=18 and hour<21:
        speak("Good evening shama")
    else:
        speak("good night")
    
    speak("jarvis at your service.please tell me how can i help you")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/welcome/Desktop/screenshot.png')




def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    speak('percentage')
    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)
    speak('percentage')

def joke():
    speak(pyjokes.get_joke())



if __name__=="__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        #all commands will be stores in lower case in query
        #for each recognition

        if 'time' in query: #tell us time when asked
            time_()
        elif 'date' in query: # tell us date when asked
            date_()
        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)


        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            # chromepath is the location of the chrome installed in the computer
            search =TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        elif 'search youtube' in query:
            speak('what should i search?')
            search_Term = TakeCommand().lower()
            speak('here we go to youtube!')
            wb.open('https://www.youtube.com/results?search_query='+search_Term)
        elif 'search google' in query:
            speak('what should i search')
            search_Term = TakeCommand().lower()
            speak('searching....')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline Partner. Take care see you soon. Bye')
            quit()
        elif 'words' in query:
            speak('opening Ms word....')
            ms_word='C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Office Word 2007.exe'
            os.startfile(ms_word)
        elif 'write a note' in query:
            speak("what should i write,shama")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("shama should i include date and time")
            ans=TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('done taking notes,STRI')
            else:
                 file.write(notes)

                

        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak('what should I remember?')
            memory = TakeCommand()
            speak('you asked me to remember that'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You aked me to remember that')


        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query= query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('the answer is :'+answer)
            speak('the answer is:'+answer)


        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")
       

        
