import random


def main():
    even = 0;
    odd = 0;
    for i in range(0, 100):
        x = random.randint(0, 36)
        if x != 0:
            if x % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        print("The winner is", x, pocket_color(x))
    print("Even: ", even, " Odd: ", odd)


def pocket_color(user_pocket_number):
    if user_pocket_number >= 0 and user_pocket_number <= 36:

        if user_pocket_number == 0:
            user_pocket_color = "green"

        elif user_pocket_number >= 1 and user_pocket_number <= 10:
            if user_pocket_number % 2 == 0:
                user_pocket_color = "black"
            else:
                user_pocket_color = "red"

        elif user_pocket_number >= 11 and user_pocket_number <= 18:
            if user_pocket_number % 2 == 0:
                user_pocket_color = "red"
            else:
                user_pocket_color = "black"

        elif user_pocket_number >= 19 and user_pocket_number <= 28:
            if user_pocket_number % 2 == 0:
                user_pocket_color = "black"
            else:
                user_pocket_color = "red"

        elif user_pocket_number >= 29 and user_pocket_number <= 36:
            if user_pocket_number % 2 == 0:
                user_pocket_color = "red"
            else:
                user_pocket_color = "black"

    if user_pocket_number >= 37:
        user_pocket_color = "Error Please enter a number between 0- 36"
    return user_pocket_color


main()