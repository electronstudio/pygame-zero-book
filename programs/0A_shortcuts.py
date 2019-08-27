# f is an easy way to insert variables into strings
score = 56
name = "Richard"
message = f"{name} scored {score} points"
print(message)

# += is an easy way to increase the value of a variable
score = score + 10  # hard way
score += 10         # easy way
print(score)

# double / means whole number division, no decimals
x = 76 // 10
# MODULO is the percent sign %. It means do division and take the remainder.
remainder = 76 % 10
print(f"76 divided by 10 is {x} and the remainder is {remainder}")

WIDTH = 500
a = 502
b = 502
# Modulo is often used as a shortcut to reset a number back
# to zero if it gets too big.  So instead of:
if a > WIDTH:
    a = a - WIDTH
# You could simply do:
b = b % WIDTH
print(a, b)

# input() takes a string argument which it prints out.
# Instead of:
print("Enter a number")
num = input()
# You can have a single line:
num = input("Enter a number")
