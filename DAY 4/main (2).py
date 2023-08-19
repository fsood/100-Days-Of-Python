import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_index = int(random.random() * len(names))
random_name = names[random_index]

print(random_name + " " "is going to pay for food today")