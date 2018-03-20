
name1 = (input("Enter your name: ").lower())
name2 = (input("Enter name of your crush: ").lower())

name1_list = list(name1)
name2_list = list(name2)

vowel_list = ["a", "e", "i", "o", "u", "y"]
consonant_list = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "l"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main():
    points = 0
    if name1_list[0] == name2_list[0]:
        points += 20
    if name1_list[0] and name2_list[0] in vowel_list:
        points += 15
    if name1_list[0] and name2_list[0] in consonant_list:
        points += 15
    if "i" or "o" or "v" or "e" in name1 and name2:
        points += 10

    vowel1_count = 0
    vowel2_count = 0          
    for vowel in vowel_list:
        if vowel in name1_list:
            vowel1_count += name1_list.count(vowel)
        if vowel in name2_list:
            vowel2_count += name2_list.count(vowel)
    if vowel1_count == vowel2_count:
        points += 20
    
    consonant1_count = 0
    consonant2_count = 0          
    for consonant in consonant_list:
        if consonant in name1_list:
            consonant1_count += name1_list.count(consonant)
        if consonant in name2_list:
            consonant2_count += name2_list.count(consonant)
    if consonant1_count == consonant2_count:
        points += 20
    
    print("\nYou and your crush fit together in " + str(points) + " %")
    if points > 75:
        print("\nLovers may be - and indeed generally are - enemies, but they never can be" 
            "friends, because there must always be a spice of jealousy and a something of" 
            "self in all their speculations.")

main()