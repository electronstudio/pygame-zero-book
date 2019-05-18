import random

n = random.randint(0, 10)

print("What is", n, "plus 7?")
g = int(input())  # why do we use int() here?
if g == n + 7:
    print("correct")
else:
    print("wrong")
