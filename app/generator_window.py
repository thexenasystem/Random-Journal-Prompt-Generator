from app.prompt_list import journal_prompts
import tkinter as tk
from tkinter import Canvas, Label, Tk
from tkinter import *
from tkinter import messagebox

import random
import string

class Generator:

#following tk tutorial https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
#^used as much as possible, now going off of https://www.askpython.com/python-modules/tkinter/random-facts-machine

    #def init?

    window=Tk()
    window.geometry("700x250")
    #window.config(big="#E67E22
    window.resizable(width=False, height=False)
    window.title('Random Journal Prompt Generator')
    window.mainloop() # is this needed?

    #labeling letting the user know what the displayed text is
    l1 = tk.Label(window,text="Random Journal Prompt:", font=("Arial", 25), fig="Black", bg="White")

    # button to be selected to return new journal prompt
    btn1=Button(window, text="Get New Prompt", font="Arial", fg='blue')
    #btn1.place(x=80, y=150)

    #text displaying the random journal_prompt
    txt1 = tk.Text(window,width=60, height=2, font=("Arial", 15), state='disabled', bg="purple")



    l1.pack()
    btn1.pack()

    def getNewPrompt(self):
        """Returns a new random journal prompt."""

       msg = messagebox.showinfo(random.choice(journal_prompts))
