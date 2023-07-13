import pyttsx3
import os
import random
from datetime import datetime
import webbrowser

def speak(sp):
    engine=pyttsx3.init()
    engine.say(sp)
    print(sp)
    engine.runAndWait()


speak("hi i am a chatbot you can chat with me please enter your name")
user_name=input("enter your name:")

speak("I will remember your name next time\n")

file_size=os.path.getsize("anshuman.txt")

user_name_file=open("anshuman.txt",'w')
user_name_file.write(user_name)
user_name_file.close()

while True:
    main = input("you:")

   
    a1=["hi","hello","hey"]
    a2=["what is the current time"]
    a3=["google"]
    a4=["add two numbers"]
    a5=["how are you"]
    a6=["good morning chatbot"]
    a7=["what is your name?"]
    a8=["see you later"]

    if main.lower() in a1:
        rand=random.choice(a1)
        speak(rand)

    elif main.lower() in a2:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak("the time is") or speak(current_time)

    elif main.lower() in a3:
        get=webbrowser.open("www.google.com",new=2)
    
    elif main.lower() in a4:
        first_number=input("enter first number:")
        second_number=input("enter second number:")
        result= float(first_number)+ float(second_number)
        speak(result)

    elif main.lower() in a5:
        bot_1 = ['I am good']
        print('Bot replied to Anshuman : ')
        speak(bot_1)

    elif main.lower() in a6:
        bot_2 = ['good morning sir,how may can i help you']
        print('Bot replied to Anshuman : ')
        speak(bot_2)

    elif main.lower() in a7:
        bot_3 = ['You call me dinobot']
        print('Bot replied to Anshuman : ')
        speak(bot_3)

    elif main.lower() in a8:
        bot_4 = ['Have a good day sir']
        print('Bot replied to Anshuman : ')
        speak(bot_4)



