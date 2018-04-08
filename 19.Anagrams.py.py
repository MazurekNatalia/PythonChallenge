import random
import os

class operations:
	def create_anagram(self, single_word):
		letters = list(single_word)
		new_word = random.sample(letters, len(letters))
		print('\nThis is your new word: ' + ''.join(new_word))

	def check_if_anagrams(self, first_word, second_word):
		first_word_sorted = sorted(list(first_word))
		second_word_sorted = sorted(list(second_word))
		if first_word_sorted == second_word_sorted:
			print("\nThese words are anagrams :)")
		else:
			print("\nThese words are not anagrams :(")


use = operations()
os.system('cls')
print('What do you want to do ? (type 1 or 2)')
print('1. Create an anagram.')
print('2. Check if two words are anagrams.')
choice = input('')

if choice == '1':
	print("\nEnter word: ")
	single_word = input()
	if ' ' not in single_word:
	    use.create_anagram(single_word)
	else:
		print("\nAre you sure it's a single word ?")

elif choice == '2':
	print("\nEnter first word: ")
	first_word = input('')
	print("\nEnter second word: ")
	second_word = input('')
	if ' ' not in first_word and ' ' not in second_word:
	    use.check_if_anagrams(first_word, second_word)
	else:
		print("\nYou should enter SINGLE words.")
else:
	print('\nWrong value.')