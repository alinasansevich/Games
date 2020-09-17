"""
Created on Thu Sep 12 14:41:05 2019

Hangman is a guessing game for two or more players.

In this version of the game, the computer selects a word from a list
at random and all players try to guess it by suggesting letters,
within a certain number of guesses.

@author: alina
"""

import time
import random
import hangman_functions as hf
from player import Player


# The program begins
# Ask how many players will play
number_of_players = int(input("Hello, welcome to Hangman!\nHow many people will be playing today?: "))

# all_players is a list of Players
all_players = []
print("OK, good!")
print("Please enter the names of the {} player(s), one at a time".format(number_of_players))
for num in range(number_of_players):
	all_players.append(Player(input("name: ")))
print("So today's players are:")
for item in all_players:
	print("\t" + item.name.capitalize())
print("\nLet's start playing!")

		
####### TO DO: add words to the list!
list_of_words = ["apple", "banana", "coconut"]#, "dolphin", "elephant", "flower", "goat", "hat", "igloo???", "jet", "kite", "lolipop???"]
lista_de_palabras = []

# PARA DESPUES: choose language 
# ask for input english/spanish, and continue game in the chosen language
time.sleep(1)
print("OK, here it goes, good luck!")

# choose a word from list_of_words
index_word_to_guess = random.randint(0, len(list_of_words) - 1)
word_to_guess = list_of_words[index_word_to_guess]
word_in_progress = len(word_to_guess) * '-'
# tell the players how long is the word chosen
print("It's a {} letter word:".format(len(word_to_guess)))
print("\n\t" + word_in_progress + "\n")

# The game starts here:
all_scores = 0

while ('-' in word_in_progress) and (all_scores != number_of_players):
    
    # if the computer wins:
    for item in all_players:
        if item.present_score == "HANGMAN":
            all_scores += 1
            if all_scores == number_of_players:
                break
    if all_scores == number_of_players:
        break
    
    # the game itself
    for item in all_players:
        if word_in_progress != word_to_guess:
            suggested_letter = input("Please choose a letter, {}: ".format(all_players[all_players.index(item)].name.title()))
            if suggested_letter in word_to_guess:
                print("Yes, good choice.\nOur word looks like this now:\n")
            else:
                print("No, no, better luck next time.")
                # end of replacement
            word_in_progress = hf.update_word(word_to_guess, word_in_progress, suggested_letter)
            print("\t" + word_in_progress + "\n")
            if '-' not in word_in_progress:
                print("You got it!")
                print("We have a winner!\n\nCongratulations, {}!\n".format(all_players[all_players.index(item)].name.title()))
                break
            if suggested_letter in word_to_guess:
                risked = hf.risk_word(word_to_guess, all_players, item)
                # word_in_progress = hf.update_word(word_to_guess, word_in_progress, suggested_letter)
                if risked == word_to_guess:
                    word_in_progress = risked
                    break

            if suggested_letter not in word_to_guess:
                item.change_score()


# if everyone lost...
if all_scores == number_of_players:
    print("\n\tOops! Looks like I won!\n")
    print('\nThe word was:\n\t')
    print('\t\t"' + word_to_guess + '"')


print("\n\n\nFinal scores:\n")
for item in all_players:
	print(item.name.title() + ':')
	print('\t' + item.present_score + '\n')