def choice():
    answer = input("")
    if answer == "1":
        first_convertion()
    elif answer == "2":
        second_convertion()
    else:
        print("You must type 1 or 2 ! Try again.")
        choice()

def first_convertion():
    try:
        celsiuses = float(input("Enter your celsius value: "))
        if celsiuses < -273.15:
            print("The value is incorrect becouse its below absolute zero ! Try again.\n")
            first_convertion()
        else:
            result_to_farenheit = (celsiuses * 1.8) + 32
            print("Your value in Farenheit is: %.2f" % result_to_farenheit)
    except ValueError:
        print("Incorrect value ! Try again.\n")
        first_convertion()

def second_convertion():
    try:
        farenheit = float(input("Enter your farenheit value: "))
        result_to_celsius = (farenheit - 32) / 1.8
        print("Your value in Celsius is: %.2f" % result_to_celsius)
    except ValueError:
        print("Incorrect value ! Try again.\n")
        second_convertion()

print("What do you want to do ?")
print("1. Convert Celsius to Farenheit.")
print("2. Convert Farenheit to Celsius.")
choice()