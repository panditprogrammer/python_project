#creating a Qr code generator
import qrcode
import os
c = 1
while (c):
	os.system("cls")
	print(" \n ******** QR CODE GENERATOR _  PanditProgrammer.Com ********** \n " )
	print("Note :- Location of Generated QR Code is same directory\n \twhere Application is Running \n ")
	print(" Get QR Code in  ' .png' format \n  ")
	string_inp = input(" Enter here to get QR code \n ")
	print("\n You have Entered : -\n  ",string_inp,"\n ")
	ar= input(" Enter Your Qr Code Name  to Save ")
	img = qrcode.make(string_inp)
	img.save(ar+".png")
	print(" \n QR Code Generated Successfully ")
	img.show()
	print(" \n Enter any Key to create again Or Press 'Enter' ot Quit  ")
	c=input(" ")