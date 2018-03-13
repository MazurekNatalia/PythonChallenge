import random

win = 0 
tie = 0
loss = 0

def game(win, tie, loss):
    print("\nWelcome to the Rock/Paper/Scissors game !\nYou have 3 rounds to win the game. Good luck :)\n")
    for i in range (0,3):
        computer_move = random.choice(["rock", "paper", "scissors"])
        print("Your move: ")
        gamer_move = input("")
        gamer_move = gamer_move.lower()

        if computer_move == "rock" and gamer_move == "scissors":
            print("Computer wins !\n")
            loss += 1
        elif computer_move == "rock" and gamer_move == "paper":
            print("You win !\n")
            win += 1
        elif computer_move == "paper" and gamer_move == "rock":
            print("Computer wins !\n")
            loss += 1
        elif computer_move == "paper" and gamer_move == "scissors":
            print("You win !\n")
            win += 1
        elif computer_move == "scissors" and gamer_move == "paper":
            print("Computer wins !\n")
            loss += 1
        elif computer_move == "scissors" and gamer_move == "rock":
            print("You win !\n")
            win += 1
        elif computer_move == gamer_move:
            print("It's a tie !\n")
            tie += 1
        else:
            print("\nWrong value. Do you think you're funny ?\n")
            exit()

    print("\nYour final results:\n1. Wins: " + str(win) + "\n2. Ties: " + str(tie) + "\n3. Losses: " + str(loss))


game(win, tie, loss)
