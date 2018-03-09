import random

def condition():
    attempts = 0
    for attempts in range (0,7):
        try:
            my_number = int(input("The number is: "))
            
            if my_number < number:
                print("Not enough.")
                print("Try again.\n")

            elif my_number > number:
                print("Too much.")
                print("Try again.\n")
            
            else:
                print("That's it ! Very good.")
                print("You guessed the right number in %d attempt."%t)
                break

        except ValueError:
            print("You can use only integers !")
            print("You have just wasted 1 attempt. Good job.\n")
    else:
        print("You exceeded amount of possible attempts !")
        exit()

def game():
    print("I thought a number...")
    print("Can you gess it ?")
    condition()

print('Hello to the "Higher-Lower" game !\n')
print("Your task is to guess the number drawn by computer. You have only 7 attempts.\nGood luck :)\n")

number = random.randint(0, 200)
game()