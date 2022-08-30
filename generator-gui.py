import tkinter

from tkinter import *
from tkinter.ttk import *

top = tkinter.Tk()

# Code to add widgets will go here...

#button to request a new random prompt

top = Tk()
top.geometry("100x100")
def getNewPrompt():
   msg = messagebox.showinfo(random.choice(journal_prompts))

B = Button(top, text = "New Journal Prompt", command = getNewPrompt)
B.place(x = 50,y = 50)



#text field displaying the new prompt
root = Tk()
text = Text(root)
text.insert(INSERT, getNewPrompt)
text.pack()

text.tag_add("here", "1.0", "1.4") #change this placement
text.tag_add("start", "1.8", "1.13") #change this placement
text.tag_config("here", background = "white", foreground = "black")
text.tag_config("start", background = "white", foreground = "black")
root.mainloop()

top.mainloop()