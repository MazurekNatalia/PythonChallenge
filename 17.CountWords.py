#Project made in object-oriented programming just for educational purposses (first steps)

import re

class total_amount:
    def counting_words(self, base):
        count = len(re.findall(r'[qwertyuioplkjhgfdsazxcvbnm]+', base))
        print('This sentence has: ' + str(count) + ' words.')

    def try_again(self, choice):
        if choice.lower() == "y":
            pass
        elif choice.lower() == 'n':
            exit()
        else:
            print("\nWrong value.")
            exit()

while True:
    base = input("\nEnter your sentence here: ").lower()
    sentence = total_amount()
    sentence.counting_words(base)

    print("\nDo you want to try again ? (y/n)")
    choice = input()
    sentence.try_again(choice)