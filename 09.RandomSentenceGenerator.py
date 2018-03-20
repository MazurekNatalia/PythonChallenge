import random

first_part_random = 0
second_part_random = 0

with open("Random Sentence Generator text.txt") as first_file:
    line = first_file.read().splitlines()
    first_part_random = random.choice(line)

with open("Random Sentence Generator text 2.txt") as second_file:
    line2 = second_file.read().splitlines()
    second_part_random = random.choice(line2)

print("\nThis is my life advice for you:")
print("\n"+ first_part_random + second_part_random)
print('\nEnjoy :)')