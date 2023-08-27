from prompt_list import journal_prompts
import random
import string

def get_new_journal_prompt(journal_prompts):
    """Returns a new random journal prompt."""
    
    #shuffle prompts list
    random.sample(journal_prompts, len(journal_prompts))
    #TODO: return [0] from list after shuffling
    return journal_prompts[0]