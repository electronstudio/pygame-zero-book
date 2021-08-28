for x in range(0, 10):
    print("looping", x)

# loop with step 2
for x in range(0, 10, 2):
    print("looping again", x)

# loop inside another loop
for a in range(0, 6):
    for b in range(0, 6):
        print(a, "times", b, "is", a * b)
