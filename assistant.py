import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

#print(voices[0].id)
engine.setProperty('voices', voices[0].id)



# used to speak give output and convert text into voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# used to take input from user and convert voice into text    
def takeCommand():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold=1
        audio=rec.listen(source,timeout=1,phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query=rec.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# used to wish user according to time        
def wish():
    hour=(datetime.datetime.now().hour)
    
    if (hour>=0 and hour<12):
        speak("Good Morning!")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon!")
    elif(hour>=18 and hour<24):
        speak("Good Evening!")
    else:
        speak("Good Night!")
        
    speak("Please tell me how may I help you?")
        
        
if __name__ == "__main__":
    wish()
    takeCommand()
    
    
    while True:
        query=takeCommand().lower()
        
     
     #logic building
     
        if 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
            
        elif 'what is' in query:
            speak("Searching Wikipedia...")
            query=query.replace("what is", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir='C:\\Users\\HP\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open chrome' in query:
            codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            
        elif 'open notepad' in query:
            codePath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)
            
        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'open calculator' in query:
            codePath="C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)
            
        elif 'open paint' in query:
            codePath="C:\\Windows\\System32\\mspaint.exe"
            os.startfile(codePath) 
            
        elif 'open word' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
            
        elif 'open excel' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
            
        elif 'open powerpoint' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
            
        elif 'open access' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
            os.startfile(codePath)
            
        elif 'open publisher' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE"
            os.startfile(codePath)
            
        elif 'open outlook' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(codePath)
            
        elif 'open onenote' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(codePath)

            
        elif 'open outlook' in query:
            codePath="C:\\Users\\HP\\AppData\\Local\\Microsoft\\Outlook\\Outlook.exe"
            os.startfile(codePath)