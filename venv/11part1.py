import random

number = (random.randrange(1,11))

print("I'm thinking of a number between 1 and 10")

while True:
    guess = input("Please guess what it is:\n")
    if int(guess) > number:
        print("that's too high")
    elif int(guess) < number:
        print("That's too low")
    elif int(guess) == number:
        print("that's it you got it!")
        answer = input("want to keep playing?:\n")
        if answer == 'yes':
            number = (random.randrange(1,11))
            True
        elif answer == 'no':
            break

