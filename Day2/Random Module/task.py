import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.my_favourite_number)

# multiple with 10 to return 0 to 10
#return the range of value you know very sure
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

#return a float number
# random_float = random.uniform(1, 10)
# print(random_float)

# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("head")
# else:
#     print("tail")

#Who gonna pay a bill
friends = ["Alice", "Bronx", "Charlie", "Danny", "Emmy", "Johnny", "Kenny"]

# first way
print("Staff will pick up one of them tppay the bill: " + friends[random.randint(0, len(friends))])

# second way
print("The next one who pay the bill: " + random.choice(friends))