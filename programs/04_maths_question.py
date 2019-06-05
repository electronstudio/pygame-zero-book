import random

n = random.randint(0, 10)

print("What is", n, "plus 7?")
g = int(input())  # Why do we use int() here?
if g == n + 7:
    print("Correct")
else:
    print("Wrong")
