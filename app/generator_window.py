from app.prompt_list import journal_prompts
import tkinter as tk
from tkinter import Canvas, Label, Tk
from tkinter import *
from tkinter import messagebox

import random
import string

class Generator:

#following tk tutorial https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

    #def init?

    window=Tk()
    #TODO: add widgets here

    # TODO: open with a prompt automatically displayed
    # text/messagebox of randomly generated journal prompt - NOT label, but maybe also label
    # print(journal_prompts)
    # label = tk.Label(text="Hello, Tkinter") but instead text = journal_prompts ???

    # TODO: make a button to get a new random journal prompt
    # button to be selected to return new journal prompt
    btn=Button(window, text="Get New Prompt", fg='blue')
    btn.place(x=80, y=150)

    window.title('Random Journal Prompt Generator')
    window.geometry("300x200+10+20")
    window.mainloop()

    def getNewPrompt(self):
        """Returns a new random journal prompt."""

       msg = messagebox.showinfo(random.choice(journal_prompts))
