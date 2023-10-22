from get_new_prompt import get_new_journal_prompt
from prompt_list import journal_prompts

import kivy
import random
import string 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10)

        button = Button(text='New Journal Prompt')
        #below is for a separate press button function
        #button.bind(on_press=self.on_press_button)

        label = Label_text='Random Journal Prompt Generator'

        # how to return layout, button, label, etc all together?
        
#save string returned from get_new_prompt()
new_prompt = get_new_journal_prompt

if __name__ == "__main__":
    app = MainApp()
    app.run()
    

