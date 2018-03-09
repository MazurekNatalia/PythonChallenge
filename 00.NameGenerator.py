import random

names_male = ['Adam','Artur','Bartlomiej','Borys','Cezary','Czeslaw','Daniel','Dominik',
              'Emil','Eryk','Fabian','Filip','Gracjan', 'Grzegorz','Henryk','Jacek',
              'Jerzy','Konrad','Krzysztof','Lukasz','Maciej','Nikodem','Oskar',
              'Przemyslaw','Robert','Tomasz','Wocjech','Zdzislaw']

names_female = ['Agata','Agnieszka','Aldona','Angelika','Barbara','Beata','Cecylia',
                'Dagmara','Elzbieta','Emiliana','Felicja','Gabriela','Grazyna','Helena',
                'Ilona','Jagoda','Karolina','Lidia','Maria','Natalia','Paula','Pola',
                'Roza','Sabina','Weronika','Wiktoria',]

surnames = ['Nowak','Wojcik','Kowalczyk','Wozniak','Mroz','Krupa','Kaczmarczyk','Jarosz']

def generator_male():
    name_m = random.choice(names_male)
    sur_m = random.choice(surnames)
    print(name_m + " " + sur_m )

def generator_female():
    name_f = random.choice(names_female)
    sur_f = random.choice(surnames)
    print(name_f + " " + sur_f )

def run():
    print("Select gender: ")
    print("1. Male")
    print("2. Female")
    choice = input("> ")
    if choice == "1":
        generator_male()
        exit()
    elif choice == "2":
        generator_female()
        exit()
    else:
        print("\nYou should enter 1 or 2 !\n")
        run()

run()