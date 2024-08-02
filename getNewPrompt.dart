import 'dart:math';
// TODO(thexenasystem): don't think this is importing right
import 'promptList.dart';

int getNewJournalPrompt(journalPrompts) {
  //returns random new journal prompt
  // TODO return random object from journal prompt list
  int randomPromptIndex = Random().nextInt(journalPrompts.length);
  return randomPromptIndex;
  
  print(randomPromptIndex);
};