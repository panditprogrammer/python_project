from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox

def getColor():
    color = askcolor()
    try:
    	r=int(color[0][0])
    	g=int(color[0][1])
    	b=int(color[0][2])
    	h=color[1]
    	R =(r,",",g,",",b)
    	Hentry.set(h)
    	Rentry.set(R)
    except Exception as e:
    	pass
    else:
    	pass
    finally:
    	pass
    

    
win=Tk()
win.title(" Color Picker - PanditProgrammer.com")
win.geometry("400x400")
win.config(bg="#f4e1d2")

Hentry =StringVar()
Rentry =StringVar()

labelhead =Label(win,text=" Color Picker Hex and RGB ",font="Times 22 bold",fg="#034f84",bg="#f4e1d2")
labelhead.pack(pady=15)

Hexcode= Label(win,text=" Hex Code ",font=("lucida 14 bold"),bg="#f4e1d2").pack(pady=10)
Hexcodeentry= Entry(win,font=("lucida 18 bold"),bg="#deeaee",fg="#50394c",width=25,textvariable=Hentry,justify="center").pack()

RGBCode= Label(win,text=" RGB Code ",font=("lucida 14 bold"),bg="#f4e1d2").pack(pady=10)
RGBCodeentry= Entry(win,font=("lucida 18 bold"),width=25,textvariable=Rentry,justify="center",bg="#deeaee",fg="#50394c",).pack()

Button(win,text='Select Color', command=getColor,width=20,font=("Ariel 11 bold"),bg="#ffffff",fg="#034f84",relief="flat").pack(pady=15)

endlabel=Label(win ,text="PanditProgrammer.Com",font="Helvetica 24 bold",fg="#f5ebd8",bg="#f4e1d2").pack(pady=15)
mainloop()