import random


def get_number():    # Get number from user
    while True:      # Loop until proper number
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return result


def guess():
    rnd = random.randint(1, 100)
    your_number = get_number()
    while your_number != rnd:     # Loop until user WIN
        if your_number < rnd:
            print("To small")
        elif your_number > rnd:
            print("To big!")
        your_number = get_number()
    print("You Win!")


guess()
