i = 0

for number in range(0, 101, 2):
    i = i + number

print(f"Total is: {i}")

total2 = 0

for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(f"Total2 is: {total2}")
