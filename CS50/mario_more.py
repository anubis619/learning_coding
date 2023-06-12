# asking user for the height of the pyramid

height = int(input("What is the size of the pyramid? "))
x_init = 1


while x_init <= height:
    print(" " * (height - x_init) + "#" * x_init + " " + "#" * x_init)
    x_init += 1
