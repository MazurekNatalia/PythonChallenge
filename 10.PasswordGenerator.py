import random

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',
'z','x','c','v','b','n','m']
special = ['!','@','#','$','%','&','*','?','/','~']
numbers = ['0','1','2','3','4','5','6','7','8','9']
upper_letters = []

def upper_for_list(letters):
    for letter in letters:
        upper_letters.append(letter.upper())
    return upper_letters

def main():
    password = []
    if difficulty == "1":
        for letter_easy in range(0, lenght):
            letter_easy = random.choice(letters)
            password += letter_easy
        print("\nYour easy password: " + ''.join(password) +"\n")
    
    elif difficulty == "2":
        for letter_medium in range(0, lenght):
            letter_medium = random.choice(letters) + random.choice(numbers)
            password += letter_medium
        print("\nYour medium password: " + ''.join(password[0:lenght]) +"\n")
    
    elif difficulty == "3":
        upper_for_list(letters)
        for letter_diff in range(0, lenght):
            letter_diff = random.choice(letters) + random.choice(numbers) + random.choice(special) + random.choice(upper_letters)
            password += letter_diff
        print("\nYour difficult password: " + ''.join(password[0:lenght]) +"\n")
    else:
        print("\nDifficulty = " + str(difficulty) + " ?\nThere is no such option, sorry.")

try:
    print("\nWelcome to the Password Generator.")
    while True:
        print("\nEnter 1,2 or 3 to choose difficulty of your pasword:\n1. Easy\n2. Medium\n3. Difficult")
        difficulty = input("")
        print("\nEnter preffered lenght of your password:")
        lenght = int(input(""))
        main()
        print("What do you want to do ? Try again or exit ?")
        what_now = input("")
        if "TRY" or "AGAIN" in what_now.upper():
            pass
        if what_now.upper() == "EXIT":
            exit()
        else:
            print("\nI don't know what it means.")
            exit()
except ValueError:
    print("\nSomething went wrong. You probably typed wrong value for lenght, difficulty or both.")
    exit()