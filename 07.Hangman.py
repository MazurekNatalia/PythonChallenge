import random

words = ["ambivalence", "independence", "acommodation", "compliment", "dilemma"]
hangman = (
"""
    ________
     |/   
     |
     |
     |
     |
     |
     |__

""",
"""
    ________
     |/   |
     |
     |
     |
     |
     |
     |__
""",
"""
    ________
     |/   |
     |  (*_*)
     |
     |
     |
     |
     |__

""",
"""
    ________
     |/   |
     |  (*_*)
     |    |
     |    |
     |
     |
     |__

""",
"""
    ________
     |/   |
     |  (*_*)
     |   /|
     |    |
     |
     |
     |__

""",
"""
    ________
     |/   |
     |  (*_*)
     |   /|\    
     |    |
     |
     |
     |__

""",
"""
    ________
     |/   |
     |  (*_*)
     |   /|\        
     |    |          
     |   /           
     |
     |__

""",

"""
    ________
     |/   |
     |  (x_x)        
     |   /|\           
     |    |           
     |   / \          
     |         
     |__      

""")
used_letters = []

def game():
    attempts = 0
    while True:
        letter = (input("\nYour letter: ").lower())
        used_letters.append(letter)
        if letter in word:
            letter_in_word = [index for index, value in enumerate(word) if value == letter]
            for elem in letter_in_word:
                int(elem)
                word_length[elem] = letter
            print(" ".join(word_length))
            print("\nCharacters used: " + ", ".join(used_letters))
            if word_length == word:
                print("\nCongratulations! You won !")
                exit()
        else:
            if letter.isdigit():
                print("\nIs this a letter ? ")
                pass
            elif len(letter) > 1:
                print("\nI can see " + str(len(letter)) +" characters here. ")
            print("It's not included in word.")
            print(" ".join(word_length))
            print("\nCharacters used: " + ", ".join(used_letters))
            print(hangman[attempts])
            print("You have " + str((7 - attempts)) + " attempts left")
            attempts += 1
            if attempts == 8:
                print('You have been hanged. Game over.')
                exit()

print('\nWelcome in "Hangman" game !\nYou can find a prompt about amount of letters in a word below.'
    '\nGuess word correctly before they hang YOU ! :)\n')

word = list(random.choice(words))
word_length = len(word) * "_".split(" ")
print(" ".join(word_length))
game()