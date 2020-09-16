#Make a simple game like Hangman and move towards object oriented programing.

"""Hangman is a guessing game for two or more players.
In this version of the game, the computer selects a word from a list
at random and all players try to guess it by suggesting letters,
within a certain number of guesses."""

import time
import random
import hangman_functions
from player import Player # contains class Player

########## MOVE TO ANOTHER MODULE ########
def update_word(word_to_guess, word_in_progress, suggested_letter):
	""" (str, str, str) -> str
	Updates the word being guessed after each player's turn.
	This function is called only if suggested_letter is present
	in word_to_guess."""
	
	word_guessed = list(word_in_progress)
	
	for i in range(len(word_to_guess)):
		if word_to_guess[i] == suggested_letter:
			word_guessed[i] = suggested_letter
	
	word_in_progress_2 = ''
	word_in_progress_2 = word_in_progress_2.join(word_guessed)
	word_in_progress = word_in_progress_2

	return word_in_progress
	#print("\t" + word_in_progress.capitalize() + "\n")

#####
def suggest_letter(suggested_letter):
	if suggested_letter in word_to_guess:
		print("Yes, good choice.\nOur word looks like this now:\n")
		#update_word(word_to_guess, word_in_progress, suggested_letter)
	else:
		print("No, no, better luck next time.")
		
def risk_word(word_to_guess):
	"""(str) -> str
	Ask the player if s/he wants to guess the whole word. If they take the risk and miss, their score should increase in one letter.
	"""
	wanna_risk = input("Would you like to take a risk and guess the whole word, {}?\nEnter Y/N: ".format(all_players[all_players.index(item)].name.title()))
	if wanna_risk.lower() == "y":
		take_risk = input("OK! Let's see what's on your mind: ")
		if take_risk == word_to_guess:
			print("Excellent! We have a winner!\n\nCongratulations, {}!\n".format(all_players[all_players.index(item)].name.title()))
			# COMPLETAR ACA? FIN DEL JUEGO
			word_in_progress = word_to_guess
			return word_in_progress #NO UPDATEA!!! CHECK QUE HACE ESTA LINEA
		elif take_risk != word_to_guess:
			print("No no, too bad, that's not it.")
			#change score
			item.change_score()
	else:
		print("OK, maybe next time.")
    #usar el return value de risk word para una nueva funcion q updatee word_in_progress = risked_word 
######### END MODULE ##########

# The program begins
# Ask how many players will play
number_of_players = int(input("Hello, welcome to Hangman!\nHow many people will be playing today?: "))

# get the names of all players
all_players = []
print("OK, good!")
print("Please enter the names of all {} players, one at a time".format(number_of_players))
for num in range(number_of_players):
	all_players.append(Player(input("name: ")))   #all_players is a list of Players!
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

# choose a word from list of words at random,and store that word in a variable
index_word_to_guess = random.randint(0, len(list_of_words) - 1)
word_to_guess = list_of_words[index_word_to_guess]
word_in_progress = len(word_to_guess) * '-'
# tell the players how long is the word chosen
print("It's a {} letter word:".format(len(word_to_guess)))
print("\n\t" + word_in_progress + "\n")

# The game starts here:
# players take turns to guess the word

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
		
	# the game itself:
	for item in all_players:
		if word_in_progress != word_to_guess:
			suggested_letter = input("Please choose a letter, {}: ".format(all_players[all_players.index(item)].name.title()))
			suggest_letter(suggested_letter)
			print("\t" + update_word(word_to_guess, word_in_progress, suggested_letter).capitalize() + "\n")
			word_in_progress = update_word(word_to_guess, word_in_progress, suggested_letter)
			if '-' not in word_in_progress:
				print("You got it!")
				print("We have a winner!\n\nCongratulations, {}!\n".format(all_players[all_players.index(item)].name.title()))
				break
			if suggested_letter in word_to_guess:
				risk_word(word_to_guess)
				print(word_in_progress)#borr
				word_in_progress = update_word(word_to_guess, word_in_progress, suggested_letter)
				print(word_in_progress) #NO LA ESTA UPDATEANDO!!! borrar esta linea
			if suggested_letter not in word_to_guess:
				item.change_score() # + player. si?no?
		if word_in_progress == word_to_guess:
			break
				#update_word(word_to_guess, word_in_progress, suggested_letter)

# if everyone lost...
if all_scores == number_of_players:
		print("\n\tOops! Looks like I won!\n")

	
			
# MOSTRAR SCORES DE TODOS
print("Final scores:\n")
for item in all_players:
	print(item.name.title() + ':\n')
	print('\t' + item.present_score)



			

			
			 
	


