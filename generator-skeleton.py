import random
import string

journal_prompts = ["Am I doing this for myself?", "What is my why?", "What is the long-term potential of this habit?", "Is it realistic and achievable?", "Do I have a plan?", "What challenges am I likely to encounter?", "How will I keep myself accountable?"]
# new_prompt = ''

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