import random

n = random.randint(0, 100)
guesses = 0

while True:
    guesses = guesses + 1
    print("I am thinking of a number, can you guess it?")
    g = int(input())
    if g == n:
        break
    elif g < n:
        print("too low")
    elif g > n:
        print("too high")
print("correct! you took", guesses, "guesses")
