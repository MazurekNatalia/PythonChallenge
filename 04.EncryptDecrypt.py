letters = "qwertyuiopasdfghjklzxcvbnm"
meaning = "10$8&6#^@9|2>7<*~`(53]4?/+"

def start():
    print("To encrypt press 1.\nTo decrypt press 2.")
    action = input("")
    if action == "1":
        operation_encrypt()
    elif action == "2":
        operation_decrypt()
    else:
        print("You must type 1 or 2 !")
        start()

def operation_decrypt():
    while True:
        sentence = input("Enter a sentence you want to decrypt (size of letters will be ignored):\n").lower()
        converter = str.maketrans(meaning, letters)
        print(sentence.translate(converter))

        print("\nWhat do you want to do? Decrypt more or encrypt something?\nYou can also press x to end the program.")
        choice = input("")
        if choice.upper() == "DECRYPT":
            pass
        elif choice.upper() == "ENCRYPT":
            operation_encrypt()
        elif choice.upper() == "X":
            exit()
        else:
            print("The value is not allowed.")
            exit()

def operation_encrypt():
    while True:
        string = input("Enter a sentence you want to encrypt (size of letters will be ignored):\n").lower()
        converter = str.maketrans(letters, meaning)
        print(string.translate(converter))

        print("\nWhat do you want to do? Encrypt more or decrypt something?\nYou can also press x to end the program.")
        sec_choice = input("")
        if sec_choice.upper() == "DECRYPT":
            operation_decrypt()
        elif sec_choice.upper() == "ENCRYPT":
            pass
        elif sec_choice.upper() == "X":
            exit()
        else:
            print("The value is not allowed.")
            exit()

start()
