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
    #building of main layout
    def build(self):
        main_layout = BoxLayout(padding=10)

        main_layout.add_widget(button)
        button = Button(text='New Journal Prompt')
        button.bind(on_press=self.on_press_button)

        main_layout.addwidget(label)
        label = Label_text='Random Journal Prompt Generator'

        return main_layout
    
    #event for pressing the button to get a new prompt
    def on_press_button_(self, instance):

        #save string returned from get_new_prompt()
        new_prompt = get_new_journal_prompt(journal_prompts)

        print(new_prompt)


if __name__ == "__main__":
    app = MainApp()
    app.run()
    

