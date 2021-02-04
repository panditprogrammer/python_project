from tkinter import * 
import time
def times():
	current_time = time.strftime("%I:%M:%S")
	clock_label = Label(win,bg="#dcedfa",fg="#000000",font="lucida 80 bold",text=current_time)
	clock_label .after(200,times)
	clock_label.grid(row=2,column=2)

win = Tk()
win.title("Digital Clock  : PanditProgrammer.Com")
win.config(bg="#dcedfa")
times()
win.mainloop()