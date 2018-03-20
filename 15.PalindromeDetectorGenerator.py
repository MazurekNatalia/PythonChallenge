import time
import random

alphabet_piece = list('abcdefghijklmnoprstuwz')
palindromes = ['civic', 'noon', 'level', 'kayak', 'noon', 'rotor', 'madam', 'radar', 'minim',
               'alula', 'sedes', 'sexes', 'torot', 'tenet', 'refer', 'malam', 'lemel', 'hannah',
               'deified', 'dewed', 'repaper', 'testset', 'toot', 'reviver', 'redder',
               'poop', 'peep']
new_word_meaning = {}

def palindrome_detector(word):
    time.sleep(2)
    if word == word[::-1]:
        print('This is a palindrome.')
    else:
        print('This is not a palindrome.')

def new_palindrome_generator():
    result = []
    result_reverse = []
    sample_length = random.randint(2,5)
    for i in range(sample_length):
        letters = random.choice(alphabet_piece)
        result += letters
    for a in range(0, sample_length -1):
        result_reverse.append(result[a])
    result.extend(result_reverse[::-1])
    final_word = ''.join(result)
    time.sleep(1)
    print('\nYour new palindrome word is: ' + final_word +'.')
    print('What is the meaning of this word ?')
    meaning = input('')
    new_word_meaning.setdefault(final_word, meaning)


print('\nWelcome in "Palindrome Specialist" program.\nSelect an option that matches your needs.')
while True:
    print('\n1. Palindrome detector\n2. Palindrome word generator')
    choice = input('\nYour choice: ').lower()
    if choice in ['1', 'palindrome detector', 'detector']:
        print('\nYou chose Palindrome Detector. \nEnter a word or sentence you want to check.')
        word = input('').lower().replace(' ', '')
        palindrome_detector(word)
    elif choice in ['2', 'palindrome generator', 'generator']:
        print('\nWhat do you want to do ? (type 1 or 2)')
        print('1. Generate a known word.\n2. Generate new word.')
        what_to_do = input()
        if what_to_do == '1':
            time.sleep(1)
            print('\nThis is your palindrome: ' + random.choice(palindromes))
        elif what_to_do == '2':
            new_palindrome_generator()
        else:
            print("\nWrong value.")
    else:
        print('\nWrong value.')
    
    time.sleep(2)
    print('\nDo you want to try again (y or n)?\nOr maybe you want to remind yourself all the words you created (r)?')
    answer = input('')
    if answer == 'Y'.lower():
        pass
    elif answer == 'N'.lower():
        break
    elif answer == "R".lower():
        print(new_word_meaning)
        break
    else:
        break 