#imoort packages
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename #save and open file
import os #open file path


#created function to create new file
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

#created function to open file
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

#created function to save file
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

#created function for quite and editing
def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<Cut>"))

def copy():
    TextArea.event_generate(("<Copy>"))

def paste():
    TextArea.event_generate(("<Paste>"))



#Created text area
root = Tk()
root.title("Untitled - Notepad")
root.geometry("644x788")

TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

#created menubar
MenuBar = Menu(root)


FileMenu = Menu(MenuBar, tearoff=0)

#menu for new file
FileMenu.add_command(label="New", command=newFile)

#menu for open file
FileMenu.add_command(label="Open", command = openFile)

#menu for save fle
FileMenu.add_command(label = "Save", command = saveFile)
FileMenu.add_separator()

#menu for exit
FileMenu.add_command(label = "Exit", command = quitApp)
MenuBar.add_cascade(label = "File", menu=FileMenu)


#menu for editing text
EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label = "Cut", command=cut)
EditMenu.add_command(label = "Copy", command=copy)
EditMenu.add_command(label = "Paste", command=paste)
MenuBar.add_cascade(label="Edit", menu = EditMenu)


#saved menubar
root.config(menu=MenuBar)


#created crollbar 
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()

