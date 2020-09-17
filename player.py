class Player():
	def __init__(self, name):
		self.name = name
		self.present_score = "-------"
		
		# I need to go from "-------" to "HANGMAN", so if suggested_letter not in word_to_guess, self.present_score = "H------"
			
	def change_score(self):
		"""Changes the score when the player suggests a letter
        that is not present in word_to_guess."""
		global present_score
		if self.present_score == ("-" * 7):
			self.present_score = "H------"
			print("Your score:\n" + self.present_score)
		elif ("-" * 6) in self.present_score:
			self.present_score = "HA-----"
			print("Your score:\n" + self.present_score)
		elif ("-" * 5) in self.present_score:
			self.present_score = "HAN----"
			print("Your score:\n" + self.present_score)
		elif ("-" * 4) in self.present_score:
			self.present_score = "HANG---"
			print("Your score:\n" + self.present_score)
		elif ("-" * 3) in self.present_score:
			self.present_score = "HANGM--"
			print("Your score:\n" + self.present_score)
		elif ("-" * 2) in self.present_score:
			self.present_score = "HANGMA-"
			print("Your score:\n" + self.present_score)
		elif ("-" * 1) in self.present_score:
			self.present_score = "HANGMAN"
			print("Your score:\n" + self.present_score)
