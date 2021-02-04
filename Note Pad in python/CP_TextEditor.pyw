
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


#creating a new file
def newFile():
    global file
    win.title("Untitled - Notepad_PanditProgrammer.com")
    file = None
    TextArea.delete(1.0, END)
def newFilekey(e):
    global file
    win.title("Untitled - Notepad_PanditProgrammer.com")
    file = None
    TextArea.delete(1.0, END)
    #print("newfile Working")

def newFileMenu():
    global file
    win.title("Untitled - Notepad_PanditProgrammer.com")
    file = None
    TextArea.delete(1.0, END)


#opening a file
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
        TextArea.delete(1.0, END)
        f = open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()

        #print("opened")
def openFilekey(e):
    global file
    file = askopenfilename(defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
        TextArea.delete(1.0, END)
        f = open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()
        #print("opened")


#Saving As file 
def SaveAs():
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    try:
        with open(file, "a") as f:
            f.write(TextArea.get(1.0, END))
            win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
            #print("File Saved type As")
    except Exception as e:
	    #print(e,"\n file can't save ")
        pass
    else:
        pass
    finally:
        pass



#save as using shortcut key
def SaveAskey(e):
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    try:
        with open(file, "a") as f:
            f.write(TextArea.get(1.0, END))
            win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
            #print("File Saved type As")
    except Exception as e:
	    #print(e,"\n file can't save ")
        pass

    else:
        pass
    finally:
        pass
    


def SaveAsRight():
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    with open(file, "a") as f:
        f.write(TextArea.get(1.0, END))
        win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
        #print("File Saved type As")
    

#saving a file
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
                win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
                #print("File Saved")
    else:
        #print("Save modified file")
        pass


#saving a file using shortCut key
def saveFilekey(e):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
                win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
                #print("File Saved")
    else:
        #print("Save modified file")
        pass

def saveFileRight():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
                win.title(os.path.basename(file) + " - Notepad_PanditProgrammer.com")
                #print("File Saved")
    else:
        #print("Save modified file")
        pass


#defining select all 
def select_all():
    TextArea.tag_add(SEL, "1.0", END)
    TextArea.mark_set(INSERT, "1.0")
    TextArea.see(INSERT)
    #print("select All")


def quitApp(e=None):
    win.destroy()

def cut():
    TextArea.event_generate("<Control-x>")
    #print("Cut")

def copy():
    TextArea.event_generate("<Control-c>")
    #print("copy")

def paste():
    TextArea.event_generate("<Control-v>")
    #print("paste")




def about():
    showinfo("Developer Info :", " Notepad by PanditProgrammer\n Version 1.0 \n Date: 23/10/2020 ")

def copyright():
    showinfo("CopyRight (c) :","All Rights are Reserved by PanditProgrammer.com\nPersonal user Only")




if __name__ == '__main__':
    #Basic tkinter setup
    win = Tk()
    win.title(" Notepad_PanditProgrammer.com")
    # win.wm_iconbitmap("Notepad_PP.ico")
    win.geometry("800x600")

    

    #right click menu bar 
    m = Menu(win, tearoff = 0) 
    m.add_command(label =" Select all    (Ctrl+A) ",command=select_all,font = ('Verdana', 11)) 
    m.add_command(label =" Cut          (Ctrl+X) ",command=cut,font = ('Verdana', 11)) 
    m.add_command(label =" Copy         (Ctrl+C) ",command=copy,font = ('Verdana', 11)) 
    m.add_command(label =" Paste        (Ctrl+V) ",command=paste,font = ('Verdana', 11)) 
    m.add_command(label =" Save         (Ctrl+S) ",command=saveFileRight,font = ('Verdana', 11)) 
    m.add_command(label =" Save As    (Ctrl+Shift+s)",command=SaveAsRight,font = ('Verdana', 11)) 
    
    
    def do_popup(event): 
        try: 
            m.tk_popup(event.x_root, event.y_root) 
        finally: 
            m.grab_release() 
    
    win.bind("<Button-3>", do_popup)





    #Add TextArea
    TextArea = Text(win, font="Arial, 16",relief=RIDGE,borderwidth=5)
    file = None
    TextArea.pack(expand=True, fill=BOTH,)

    # Lets create a menubar

#Main menu bar
    MenuBar = Menu(win)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="  New        (Ctrl+N) ", command=newFile,font = ('Verdana', 11))
    
    #To Open already existing file
    FileMenu.add_command(label="  Open       (Ctrl+O)  ", command = openFile,font = ('Verdana', 11))
    
    # To save the current file

    FileMenu.add_command(label = "  Save          (Ctrl+S)  ", command = saveFile,font = ('Verdana', 11))
    
    FileMenu.add_command(label = "  Save As   (Ctrl+Shift+S)  ", command = SaveAs,font = ('Verdana', 11))
    FileMenu.add_separator()
    FileMenu.add_command(label = "  Exit           (Ctrl+Q)  ", command = quitApp,font = ('Verdana', 11))
    MenuBar.add_cascade(label = "  File  ", menu=FileMenu,font = ('Verdana', 14))
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "  Select All     (Ctrl+A)  ",command=select_all,font = ('Verdana', 11))
    
    EditMenu.add_command(label = "  Cut            (Ctrl+X)  ", command=cut,font = ('Verdana', 11))
    
    EditMenu.add_command(label = "  Copy          (Ctrl+C)  ", command=copy,font = ('Verdana', 11))
    
    EditMenu.add_command(label = "  Paste         (Ctrl+V)  ", command=paste,font = ('Verdana', 11))
    
    MenuBar.add_cascade(label="  Edit  ", menu = EditMenu,font = ('Verdana', 14))



    # Setting Menu Starts
    SettingMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    SettingMenu.add_command(label = "  Font       ",font = ('Verdana', 11))
    
    SettingMenu.add_command(label = "  Theme          ",font = ('Verdana', 11))
    
    #SettingMenu.add_command(label = "  Copy          ",font = ('Verdana', 11))
    
    #SettingMenu.add_command(label = "  Paste         ", command=,font = ('Verdana', 11))
    
    MenuBar.add_cascade(label="  Setting  ", menu = SettingMenu,font = ('Verdana', 14))
    # Setting Menu Ends




    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "  About Notepad  ", command=about,font = ('Verdana', 11))
    HelpMenu.add_command(label = "  About Copyrights  ", command=copyright,font = ('Verdana', 11))
    MenuBar.add_cascade(label="  Help  ", menu=HelpMenu,font = ('Verdana', 14))
    # Help Menu Ends



    win.config(menu=MenuBar)
    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set,)
    TextArea.bind("<Control-s>",saveFilekey)
    TextArea.bind("<Control-n>",newFilekey)
    TextArea.bind("<Control-o>",openFilekey)
    # TextArea.bind("<Control-Shift-s>",SaveAskey)
    TextArea.bind("<Control-q>",quitApp)
    

    win.mainloop()