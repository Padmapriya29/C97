import random

print("Number Guessing Game")

number= random.randint(1,9)

chances = 0

print("Guess a number(Between 1 to 9):")

while chances < 5:

    guess = int(input("Enter your guess:"))

    if guess == number:
        print("Congratulations You Won!")
        break

    elif guess < number:
        print("Your guess was low: guess a number lower than that")

    else:
        print("Your guess was high: guess a number higher than that")

    chances+=1

if not chances < 5:
    print("You lose")
