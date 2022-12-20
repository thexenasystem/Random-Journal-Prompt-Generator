from app.prompt_list import journal_prompts
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import random
import string

"""
journal_prompts = [["this is prompt one"], 
    ["this is prompt two"], 
    ["look! it's the third prompt!"], 
    ["and this is the fourth prompt"],
    ["gonna make so many promppttsssssss"],
    ["this list is gonna be huge"],
    ["but not in a trump way"],
    ["how is your day going?"],
    ["what would you like to change about today?"],
    ["how are you feeling this morning?"],
    ["what are five things you love about yourself?"],
    ["what is a pet peeve of yours?"],
    ["what is the most frustrating thing about your job?"],
    ["what is the best thing about your job?"],
    ["even more journal prompts"],
    ["all of the journal prompts"],
    ["can't decide if this should be in it's own file or the main file"],
    ["chips are really good"]]
"""

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

