from app.prompt_list import journal_prompts
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import random
import string

def prompt_window():
    """Creates the prompt window and displays random journal prompt."""

    #TODO:code to initiate tkinter window
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


def getNewPrompt():
    """Returns a new random journal prompt."""
   msg = messagebox.showinfo(random.choice(journal_prompts))

