def collatz():
    global number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
            collatz()
        
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
            collatz()

print("Enter integer: ")
try:
    number = int(input("> "))
    collatz()
except ValueError:
    print("Don't you know what integer is ?")