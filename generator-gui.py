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

top.mainloop()