import tkinter

from tkinter import *
from tkinter.ttk import *

top = tkinter.Tk()

# Code to add widgets will go here...

top.mainloop()

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

# EXAMPLE CODE FROM TKINTER TUTORIAL  

    #def calculate(*args):
    #try:
        #value = float(feet.get())
        #meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    #except ValueError:
        #pass

#root = Tk()
#root.title("Feet to Meters")

#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

#feet = StringVar()
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#meters = StringVar()
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#for child in mainframe.winfo_children(): 
    #child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
#root.bind("<Return>", calculate)

#root.mainloop()