''' A small program that will evaluate to odds or even based on the input from the user'''

user_input = int(input("Which number do you want to check? "))

user_input = user_input % 2

if user_input == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
