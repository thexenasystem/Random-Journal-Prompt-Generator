import tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = tkinter.Tk()

import random
import string

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

#def get_new_prompt():
    #selected_prompt = random.choice(journal_prompts)
    #return selected_prompt

print("Would you like a new journal prompt? Push Y for yes and N for no.")
response = input()

if response is 'Y':
    print(random.choice(journal_prompts))

elif response is 'N':
    print("You have selected no.")

elif response != 'Y' and response != 'N':
    print('Error. Incorrect input. Please hit "Y" for yes and "N" for no.')

#button to request a new random prompt

top = Tk()
top.geometry("100x100")
def getNewPrompt():
   msg = messagebox.showinfo(random.choice(journal_prompts))

B = Button(top, text = "New Journal Prompt", command = getNewPrompt)
B.place(x = 50,y = 50)
top.mainloop()

#text field displaying the new prompt
root = Tk()
text = Text(root)
text.insert(INSERT, getNewPrompt)
text.pack()

text.tag_add("here", "1.0", "1.4") #change this placement, needs to fit the size of any prompt
text.tag_add("start", "1.8", "1.13") #change this placement, needs to fit the size of any prompt
text.tag_config("here", background = "white", foreground = "black")
text.tag_config("start", background = "white", foreground = "black")
root.mainloop()

top.mainloop()
