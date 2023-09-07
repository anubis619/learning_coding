'''For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

To a count how many times the following letters appear: TRUE + LOVE
'''

# first_name = input("What is your name? ")
# second_name = input("What is their name? ")

first_name = "David Beckham"
second_name = "Victoria Beckham"

concat_name = first_name + second_name
concat_name = concat_name.lower()


def love_calc(word, t):
    return word.count(t)


count_t = love_calc(concat_name, "t")
count_r = love_calc(concat_name, "r")
count_u = love_calc(concat_name, "u")
count_e = love_calc(concat_name, "e")
count_l = love_calc(concat_name, "l")
count_o = love_calc(concat_name, "o")
count_v = love_calc(concat_name, "v")

print(count_t, count_r, count_u, count_e, count_l, count_o, count_v, count_e)
sum_letters = str(count_t + count_r + count_u + count_e) + \
    str(count_l + count_o + count_v + count_e)
print(sum_letters)
sum_letters = int(sum_letters)

if sum_letters < 10 or sum_letters > 90:
    print(
        f'Your score is {sum_letters}, you go together like coke and mentos.')
elif sum_letters > 40 and sum_letters < 50:
    print(f'Your score is {sum_letters}, you are alright together.')
else:
    print(f'Your score is {sum_letters}.')
