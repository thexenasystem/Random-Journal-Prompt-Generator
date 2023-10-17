from get_new_prompt import get_new_journal_prompt
import tkinter as tk
from tkinter import *


import random
import string 

#def main() :

#create window
window=tk.Tk()

#create text widget
text_widget = Text(window, height = 5, width = 52)

#create label
prompt_text = tk.Label(text="Random Journal Prompt:")

#print string returned from get_new_prompt()
new_prompt = print(get_new_journal_prompt)

#create button to get next random prompt
button1 = Button(window, text = "Next")

prompt_text.pack()
text_widget.pack()
button1.pack()

#text_widget.insert("1:0", new_prompt)

#TODO: button function text_widget.delete to clear the box, then display next prompt

window.mainloop()

#if __name__ == "__main__":
    #main()

