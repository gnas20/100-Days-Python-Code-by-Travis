#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word=word_list[random.choice(word_list)]

guess_choice=input("Enter your guessing word? ").lower()

if chosen_word==guess_choice:
    print("You guess correctly!")
else:
    print("It doesn't match!")

