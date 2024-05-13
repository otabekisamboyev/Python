import random

names_string = input("Give me everybody's name, seperated by comma: ")
names = names_string.split(", ")

# volunteer = random.randint(0, len(names) - 1)
# print(f"{names[volunteer].title()} is going to buy the meal today!")

volunteer = random.choice(names)
print(f"{volunteer.title()} is going to buy the meal today!")


