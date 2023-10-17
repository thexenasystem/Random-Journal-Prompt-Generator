from get_new_prompt import get_new_journal_prompt
import tkinter as tk
from tkinter import *
from prompt_list import journal_prompts


import random
import string 

#def main() :

#create window
window=tk.Tk()

#save string returned from get_new_prompt()
new_prompt = get_new_journal_prompt

#create text widget
text_widget = Text( window, height = 5, width = 52)

#create label
prompt_text = tk.Label(text="Random Journal Prompt:")

#prompt to be displayed
Prompt = get_new_journal_prompt(journal_prompts)
#create button to get next random prompt
button1 = Button(window, text = "Next")

prompt_text.pack()
text_widget.pack()
button1.pack()

text_widget.insert(tk.END, Prompt)

#TODO: button function text_widget.delete to clear the box, then display next prompt

window.mainloop()

#if __name__ == "__main__":
    #main()

