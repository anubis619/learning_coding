'''
Goal of this little project of day 4 is to create a  game of rock paper scissors using the random number generation in Python.

'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

'''
Function to create the "UI" of the selection. Used a function as it would have been repeated code in both player and computer selection.
As such going with best standards we turn the repeated code into a function that we can call to show what the player has selected and what the computer has selected.
'''


def game_selection(x):
    if x == 0:
        print(rock)
    elif x == 1:
        print(paper)
    else:
        print(scissors)


player_option = int(input(
    "Let's play a game of Rock, Paper & Scissors. Please select 0 for Rock, 1 for Paper and 2 for Scissors: "))

# For testing purposes I added a variable that instead of asking the player for a number it will basically play "ai" vs "ai" :).
# player_option = random.randint(0, 2)


computer_number = random.randint(0, 2)


print(computer_number, player_option)

print("Your choice is:")
game_selection(player_option)

print("Computer chose:")
game_selection(computer_number)

# Pseudo code to show all the options that we have to build in the if/elseif/else statements.
'''
Pseudo code:

If player selects rock and computer selects scissors
    Player wins
If player selects rock and computer selects paper
    Player loses
If player selects paper and computer selects rocks
    Player wins
If player selects paper and computer selects scissors
    Player loses
If player selects scissors and computer selects paper
    Player loses
If player selects scissors and computer selects rock
    Player wins
Else
    Should be a draw

'''


if player_option == 0 and computer_number == 1:
    print("You lose.")
elif player_option == 0 and computer_number == 2:
    print("You win.")
elif player_option == 1 and computer_number == 0:
    print("You win.")
elif player_option == 1 and computer_number == 2:
    print("You lose.")
elif player_option == 2 and computer_number == 0:
    print("You lose.")
elif player_option == 2 and computer_number == 1:
    print("You win.")
else:
    print("It is a draw.")
