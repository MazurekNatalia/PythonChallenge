import re

vowel_list = ["a", "e", "i", "o", "u", "y"]
consonant_list = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "l"]

def main():
    word = input("\nEnter your word: ")
    if word[0] in consonant_list:
        consRegex = re.compile(r'[^aeiouyAEIOUY]+')
        searching_consoants = consRegex.search(word)
        first_consoant_list = list(searching_consoants.group())
        word_list = list(word)
        length = len(first_consoant_list)
        del word_list[:length]
        new_word_list = word_list + first_consoant_list
        print(''.join(new_word_list) + "ay")
    else:
        print("\nThere is nothing to change :(\nCheck out 'Instruction' clause above and try again.")


print("\nWelcome to the \"Pig Latin\" - word transformation game.")
print("Instruction: You can expect changes only if your word starts with a consonant !")

while True:
    main()
    print("\nDo you want to try again ? (Y\\N)")
    choice = input("")
    if choice.upper() == "Y":
        pass
    elif choice.upper() == "N":
        break
    else:
        print("\nI don't understand that answer.")
        break
        
