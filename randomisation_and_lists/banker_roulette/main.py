import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

# Get the total number of items in list
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay the meal today!")