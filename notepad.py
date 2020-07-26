import tkinter
import tkinter.messagebox as tmsg
import tkinter.filedialog as dil
import os
def about():
    tmsg.showinfo("Notepad", "This is open do it whatever you want")

def newfile():
    global file
    main_frame.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, "end")

def openfile():
    global file
    file = dil.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        main_frame.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, "end")
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())


def save():
    global file
    if file == None:
        file = dil.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        
        if file == "":
            file = None
        
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, "end"))
            f.close()
            
            main_frame.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, "end"))
        f.close()

def quitapp():
    main_frame.destroy()

def paste():
    TextArea.event_generate(("<<Paste>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def cut():
    TextArea.event_generate(("<<Cut>>"))

main_frame = tkinter.Tk()
main_frame.geometry("700x530")
main_frame.resizable(False, False)
main_frame.title("Mynote")
#Adding textArea

scrollbar = tkinter.Scrollbar(main_frame)
scrollbar.pack(side="right",fill="y")

TextArea = tkinter.Text(main_frame, font="lucida 13",yscrollcommand = scrollbar.set)
file = None
TextArea.pack(fill="both")

scrollbar.config(command=TextArea.yview)

main_menu = tkinter.Menu(main_frame)
file_menu = tkinter.Menu(main_menu, tearoff=0)

# add option in file menu

file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= quitapp)
main_menu.add_cascade(label="File", menu=file_menu)

edit_menu = tkinter.Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
main_menu.add_cascade(label="Edit", menu=edit_menu)

help_menu = tkinter.Menu(main_menu, tearoff=0)
help_menu.add_command(label="About Notepad", command=about)
main_menu.add_cascade(label="Help", menu=help_menu)

main_frame.config(menu=main_menu)

main_frame.mainloop()