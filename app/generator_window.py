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
    def generator_window(self):
        """
        Creates the prompt window and displays a random journal prompt.
        along with a button to get a new random journal prompt.
        """

        #TODO:code to initiate tkinter window
        window=Tk()
        #TODO: add widgets here

        window.title('Random Journal Prompt Generator')
        window.geometry("300x200+10+20")
        window.mainloop()

        #TODO: open with a prompt automatically displayed

        #for if the user wants a different prompt
        #TODO: change this from a question to just a button to push for a new prompt
        print("Would you like a new journal prompt? Push Y for yes and N for no.")
        response = input()

        #TODO: delete this if statement
        if response is 'Y':
            print(random.choice(journal_prompts))
        elif response is 'N':
            print("You have selected no.")
        elif response != 'Y' and response != 'N':
            print('Error. Incorrect input. Please hit "Y" for yes and "N" for no.')


    def getNewPrompt(self):
        """Returns a new random journal prompt."""

       msg = messagebox.showinfo(random.choice(journal_prompts))
