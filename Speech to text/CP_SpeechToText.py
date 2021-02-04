import speech_recognition as sr
import os
r= sr.Recognizer()
c=1
while(c):
	os.system("cls")
	print("\n Speak and get as Text \n")
	try:
		with sr.Microphone() as source:
			
			print("\n Listening... \n")
			audio_r =r.record(source,duration =5)
			queryq =r.recognize_google(audio_r)
			print("\n \n  queryq \n \n")
	except Exception as e:
		print("Error ... ! ", e)
	print(" Enter any key to play again \n ' Hit Enter to Exit' ")
	c= input("")
	