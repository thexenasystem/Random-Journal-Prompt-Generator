from app.prompt_list import journal_prompts
from app.get_new_prompt import get_new_journal_prompt
import tkinter as tk
from tkinter import Canvas, Label, Tk
from tkinter import *
from tkinter import messagebox

import random
import string 

def main() :
    #prompt text to display in label widget
    new_prompt = print(get_new_journal_prompt)
    window=tk.Tk()
    prompt_text = tk.Label(text=new_prompt)
    prompt_text.pack()
    window.mainloop()

if __name__ == "__main__":
    main()

