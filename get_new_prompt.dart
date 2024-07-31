import 'dart:math';
//TODO how to import this list properly
import prompt_list from journal_prompts;

void get_new_journal_prompt(journal_prompts) {
  //returns random new journal prompt
  // TODO return random object from journal prompt list
  int randomIndex = Random().nextInt(prompt_list.length);
  
  print(prompt_list[randomIndex]);
};