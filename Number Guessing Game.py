import random

number = random.randint(1, 20)
attempts = 5

print("Guess the number (1–20)")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You guessed it right! 🎉")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    attempts -= 1

print("Game Over. Number was:", number)
