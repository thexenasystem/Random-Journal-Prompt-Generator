import random
import string

journal_prompts = ["This is your first journal prompt", "This is the second prompt. It has two sentences.", "This is the third prompt.", "This is the fourth prompt.", "This is the fifth prompt."]
new_prompt = ''

def get_new_prompt():
    new_prompt = random.choice(journal_prompts)
    return new_prompt

print("Would you like a new journal prompt? Push 'Y' for yes and 'N' for no.")
response = input()

if response is 'Y':
    print(new_prompt)

elif response is 'N':
    print("You have selected no.")

elif response is not 'Y' and response is not 'N':
    print('Error. Incorrect input. Please hit "Y" for yes and "N" for no.')