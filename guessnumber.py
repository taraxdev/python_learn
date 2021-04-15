import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guesss the number between 1 and {x}: "))
        if guess < random_number:
            print("Try again. Too low")
        if guess > random_number:
            print("Try again. Too High")

    print(f"Congrats for guessing correct number {random_number}")

guess(20)
