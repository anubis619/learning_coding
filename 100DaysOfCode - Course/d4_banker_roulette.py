import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

the_winner = random.randint(0, len(names))
the_winner = names[the_winner]
print(f"{the_winner} is going to buy the meal today!")
