import random

first_verse = ["In the twilight rain, ", "For love and for hate, ", "An old silent pond, ", 
               "I once had a car of no luck, ", "The sky is so blue, "]
second_verse = ["A frog jumps into the pond, ", "Swaying in the evening sun, ",
                "Past the black winter trees, ", "The sun is so warm up high ", "It got stuck in a pile of muck, "]
third_verse = ["I really like toast.", "Beans are kind to hearts.", "Splash! Silence again.", 
               "My pet dog just ate it whole.","And then do big farts! "]

def syllable_count(sentence):
    sentence = sentence.lower()
    count = 0
    vowels = "aeiouy"
    if sentence[0] in vowels:
        count += 1
    for index in range(1, len(sentence)):
        if sentence[index] in vowels and sentence[index - 1] not in vowels:
            count += 1
            if sentence.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count

beginning = random.choice(first_verse)
middle = random.choice(second_verse)
ending = random.choice(third_verse)
haiku = beginning + "\n" + middle + "\n" + ending
print("\n" + haiku)

verse_one = syllable_count(beginning)
verse_two = syllable_count(middle)
verse_three = syllable_count(ending)

if verse_one == 5 and verse_two == 7 and verse_three in [5, 6]:
	print("\nThis is your Haiku :)")    
else:
	print("\nThat's sweet but it's not Haiku actually :(")