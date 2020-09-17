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


def risk_word(word_to_guess, all_players, item):
    """(str) -> str
    Ask the player if s/he wants to guess the whole word. If they take the risk and miss, their score should increase in one letter.
    """
    wanna_risk = input("Would you like to take a risk and guess the whole word, {}?\nEnter Y/N: ".format(all_players[all_players.index(item)].name.title()))
    if wanna_risk.lower() == "y":
        take_risk = input("OK! Let's see what's on your mind: ")
        if take_risk == word_to_guess:
            print("Excellent! We have a winner!\n\nCongratulations, {}!\n".format(all_players[all_players.index(item)].name.title()))
            # COMPLETAR ACA? FIN DEL JUEGO
            return take_risk #NO UPDATEA!!! CHECK QUE HACE ESTA LINEA
        else:
            print("No no, too bad, that's not it.")
            item.change_score()
            return take_risk
    else:
        print("OK, maybe next time.")