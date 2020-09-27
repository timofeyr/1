import speech_recognition as sr
import pyttsx3
import random
import string
import time

engine = pyttsx3.init()

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
	print("Say command")
	engine.say("Say command")
	engine.runAndWait()
	audio = r.listen(source)

sentence = r.recognize_google(audio, language="ru-RU")
sentence.lower()

if sentence == "пароль":
	
	print("I am making a password and am going to guess it")
	engine.say("I am making a password and am going to guess it")
	engine.runAndWait()

	incorrectPasswords = []
	letters = ""
	password = ""
	passwordGuess = ""
	run = True

	print("Enter length of a password")
	engine.say("Enter length of a password")
	engine.runAndWait()
	length = int(input("Password length: "))

	def passwordGenerator(length):
	    global run
	    global startTime

	    startTime = time.time()

	    letters = string.ascii_lowercase
	    password = ''.join(random.choice(letters) for i in range(length))
	    print("Password is " + password)

	    print("Now let's guess")

	    while run:
	        passwordGuess = ''.join(random.choice(letters) for i in range(length))
	        if passwordGuess != password:
	            incorrectPasswords.append(passwordGuess)
	            print(passwordGuess)
	        else:
	            print(passwordGuess)
	            print("Password: " + passwordGuess)
	            print("Quantity of incorrect passwords: " + str(len(incorrectPasswords)))
	            run = False
	            break

	passwordGenerator(length)

	print(time.time() - startTime)