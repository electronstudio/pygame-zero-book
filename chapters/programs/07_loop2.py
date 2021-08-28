import random

n = random.randint(0, 100)
guesses = 0

while True:
    guesses = guesses + 1
    print("I am thinking of a number, can you guess what it is?")
    g = int(input())
    if g == n:
        break
    elif g < n:
        print("Too low")
    elif g > n:
        print("Too high")
print("Correct! You took", guesses, "guesses.")
