import random
import time

possible_answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definately', 
                    'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 
                    'Yep', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 
                    'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 
                    "Don't count on it", 'My reply is no', 'My sources say no', 
                    'Outlook not so good', 'Very doubtful']
def play():
    print("\nYour question: ")
    question = input("\n")
    amount_of_words = len(question.split())
    if amount_of_words >= 4:
        time.sleep(2)
        print(random.choice(possible_answers))
    else:
        print("Not enough words.")
        exit()

print("\nHello to the Magic 8 - Ball simulator.\nAsk me a question that possible answers are 'Yes' or 'No'.")
print("Minimum length of your question is 4 words.")
play()

while True:
    time.sleep(2)
    print("\nDo you want to ask me again (yes or no) ?")
    play_again = input()
    if play_again.upper() == "YES":
        play()
    elif play_again.upper() == "NO":
        print("Thanks for playing :)")
        exit()
    else:
        print("YES or NO - wth you don't understand ? ")
        pass