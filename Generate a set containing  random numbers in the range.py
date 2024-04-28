import random
random_numbers_set = set()
while len(random_numbers_set) < 10:
    random_number = random.randint(15, 45)
    random_numbers_set.add(random_number)

print("Original set of random numbers:", random_numbers_set)
