def test():
    print("entering function block")
    for i in range(0,10):
        print("entering for loop block")
        if i == 5:
            print("in if block")
        print("leaving for loop block")
    print("leaving function block")
print("not in any block")
test()
