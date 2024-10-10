import datetime
import os
import random
import webbrowser
from tkinter import *

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from AppOpener import open
from PIL import Image, ImageTk

# initialisation  say property
engine = pyttsx3.init()
"""VOICE GIRL"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#Speak function
def say(text):
    engine.say(f"{text}")
    engine.runAndWait()


#Action perform
def Action(query):
    while True:
        '''print("Listening...")
        query= takeCommand()'''
        query  = query.lower()

        if "website" in query:
            a=query.split()
            sites=a[1]
            #say(f"Open {sites} sir..")
            webbrowser.open(f"https://www.{sites}.com")
            return "Opening..."

        if "play music" in query:
            song=query.replace("play music","")
            pywhatkit.playonyt(song)
            return "Playing..."

        if "time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M")
            say(f"Sir the time is {strfTime}")
            return f"The time is{strfTime}"

        if "search" in query:
            topic=query.replace("search","")
            pywhatkit.search(topic)
            return print(pywhatkit.search(topic))

        if "open" in query:
            app= query.replace("open","").strip()
            open(app)
            return "Opening..."
        
        if 'who is' in query:
            name=query.replace("who is","")
            info=wikipedia.summary(name,1)
            say(info)
            return info

        if 'joke' in query:
            joke=pyjokes.get_joke()
            say(joke)
            return joke
        
        if "where is" in query:
            query= query.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(query[2])
            say("Hold on Dante, I will show you where " + query[2] + " is.")
            webbrowser.open(location_url)
            return "Opening..."

        if "what is your name" in   query :
            say("my name is Jervis")
            return "my name is Jervis"

        elif "hello" in query  or "hye" in query  or "hay" in query:
            say("Hey sir, How i can  help you !")
            return "Hey sir, How i can  help you !"

        elif "how are you" in  query :
                say("I am doing great these days sir")
                return "I am doing great these days sir"

        elif "thanku" in query or "thank" in query:
            say("its my pleasure sir to stay with you")
            return "its my pleasure sir to stay with you"

        elif "good morning" in query:
            say("Good morning sir, i think you might need some help")
            return "Good morning sir, i think you might need some help"

        elif "shutdown" in query or "quit" in query:
                say("ok sir")
                return "ok sir"
        else:
            return "Please repeat"

#speaking command
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            query= r.recognize_google(audio, language="en-in")
            if 'Jarvis' in query:
                query= query.replace('Jarvis','')
            bot_val = Action(query)
            text.insert(END, "Me --> "+query+"\n")
            if bot_val != None:
                text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
            if bot_val == "ok sir":
                root.destroy()
        except Exception as e:
            return "Can't hear you. Sorry from jarvis"

#written command
def write():
    send = entry.get()
    text.insert(END, "Me --> "+send+"\n")
    bot = Action(send)
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()

#delete message
def delete():
    text.delete("1.0", "end")


#GUI for show window

root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False,False)
root.config(bg="#6F8FAF")


# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)


# Text Lable
Text_lable = Label(Main_frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


# Image
Display_Image = ImageTk.PhotoImage(Image.open("assitant.png"))
Image_Lable = Label(Main_frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)


# Add a text widget
text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100)


# Add a entry widget
entry= Entry(root, justify = CENTER)
entry.place(x=100 , y = 500 , width= 350, height= 30)



# Add a text button1
button1 =  Button(root,  text="Speak" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command=takeCommand).place(x= 70, y= 575)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command=write).place(x= 400, y= 575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command=delete).place(x= 225, y= 575)

say("Hello I am Jarvis AI")
root.mainloop()




