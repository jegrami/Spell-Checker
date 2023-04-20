
from textblob import TextBlob 

def check_spelling():
    ''' Prompts user for a word and returns correct version if word is mispelled'''
    while True:
        word = input("Please enter a word:\n").lower()
        correct_word = str(TextBlob(word).correct())
        if correct_word != word:
           response = input(f"Did you mean {correct_word}? (yes/no):\n ").lower()
           if response == 'yes':
               return correct_word.title()
           
           elif response == 'no':
               print(f"Are you sure about {word}? Check and try again.")
        else:
            return word.title()
word = check_spelling()
print(f"The word is {word.title()}.")