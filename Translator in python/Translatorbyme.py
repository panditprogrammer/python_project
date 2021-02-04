from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#starting create GUI
root = Tk()
root.geometry("955x520")
root.config(bg = "#fffef9")
root.title("Translator - PanditProgrammer.com")
root.resizable(0,0)

# create a fro heading
Label(root, text = "Language Translator", font = "arial 20 bold",bg = "#fffef9",fg="#87bdd8").pack()

# create input box
Label(root,text ="Enter Text", font = 'arial 15 bold', bg = "#fffef9").place(x=280,y=60)

#inputtext box 
Input_text = Text(root,font = 'arial 12',bg="#f2ece6" ,height = 15, wrap = WORD,pady=5,width = 50)
Input_text.place(x=20,y=100)

Label(root,text ="Output", font = 'arial 15 bold',bg = "#fffef9").place(x=780,y=60)
# Output text box
Output_text = Text(root,font = 'arial 12',bg="#f2ece6", height = 15, wrap = WORD, pady= 5, width =50)
Output_text.place(x=480 ,y=100)



# create text box for getting input
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('Select Input Language')
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=480,y=60)
dest_lang.set('Select Output Language')


# here is Translator 
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    
    

trans_btn = Button(root, text = 'Translate',font = 'lucida 12 bold',pady = 5,command = Translate , bg = "#87bdd8", activebackground = 'sky blue',width=25)
trans_btn.place(x=338,y=400)
Label(root,text ="PanditProgrammer.Com", font = 'Helveltica 25 bold',bg = "#fffef9",fg="#f1f2db" , width = '20',pady=5).pack(side = 'bottom')

root.mainloop()