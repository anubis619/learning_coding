''' A small program to see if you are allowed to ride on the rollercoaster or not.'''

print("Welcome to the rollercoaster!")
height_check = int(input("What is you height in cm? "))

if height_check > 120:
    print("You can ride the rollercoaster!")
    check_age = int(input("What is your age? "))
    if check_age < 12:
        print("The ride ticket will be 5$.")
    elif check_age >= 12 and check_age <= 18:
        print("The ticket will cost you 7$.")
    else:
        print("The ride will cost you 12$.")
else:
    print("Sorry. You can not ride the rollercoaster.")
