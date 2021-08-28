import random

n = random.randint(0, 10)

while True:
    print("I am thinking of a number, can you guess what it is?")
    g = int(input())
    if g == n:
        break
    else:
        print("Wrong")
print("Correct!")
