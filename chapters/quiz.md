# Exercises

These exercises will test your understanding of the basics of Python.  Each exercise will ask you to write a program.  The solution is
often on the following page - do not turn the page until you have attempted your own solution!  Save each program in a separate file.

\newpage

## For loops

Run this program to see a `for` loop:

```python
for x in range(0,11):
    print(x)
```

### A baker has three customers.

He asks them each how many cakes they want
so he knows how many he must bake. He writes this program.

```python
total = 0
print("Customer", 1, "how many cakes do you want?")
cakes = int(input())
total = total + cakes
print("Customer", 2, "how many cakes do you want?")
cakes = int(input())
total = total + cakes
print("Customer", 3, "how many cakes do you want?")
cakes = int(input())
total = total + cakes
print("I will bake", total, "cakes!")
```

This program is longer than it needs to be.  Instead of typing it, write your own program using a `for` loop.  It should be only 6 (or fewer) lines long.

\newpage

A possible solution:

```python
total=0
for x in range(1, 4):
    print("Customer", x, "how many cakes do you want?")
    cakes = int(input())
    total = total + cakes
print("I will bake", total, "cakes!")
```


### The baker gets a fourth customer.

Change your program so it works for 4 customers.

### The baker has a different number of customers every day.

Change the program so it
asks how many customers there are. Store the number typed by the user in a variable
called `c`. Change the loop so it works for `c` customers rather than 4 customers.

\newpage

A possible solution:

```python
print("How many customers are there today?")
c = int(input())
total=0
for x in range(1, c+1):
    print("Customer", x, "how many cakes do you want?")
    cakes = int(input())
    total = total + cakes
print("I will bake", total, "cakes!")
```

### If a customer orders 12 cakes, he gets an extra cake for free

Use an `if` statement to check `cakes > 12`. If so, add one more cake.

## List

Rather than the user typing in data, your program might be supplied with data in a list.
Here is an list of prices  - a shopping list. Note we dont use a currency symbol except when we print the price.

```python
prices = [3.49, 9.99, 2.50, 20.00]
for price in prices:
    print("item costs £", price)
```

Change the program so that it prints the total price of all the items added together.

\newpage

A possible solution:

```python
prices = [3.49, 9.99, 2.50, 20.00]
total = 0
for price in prices:
    print("item costs £", price)
    total = total + price
print("shopping total", total)
```

There is a problem with solution, can you see what it is?

\newpage

The problem is that we are using *floating point* numbers for the prices and floating point maths in the computer is not entirely accurate, so the answer will be very slightly wrong.
One way to fix this is to round the result to two decimal places using the `round()` function:

```python
print("shopping total", round(total,2))
```

This works for a short list, but if the list was millions of items long it might not give the right result.  Can you think of a better way?

\newpage

Instead of storing the number of pounds, store the the number of pennies.  Britain no longer has a half-penny, so the numbers will always be whole numbers - *integers* - and
no floating points will be needed for the addition.

```python
prices = [349, 999, 250, 2000]
total = 0
for price in prices:
    print("item costs £", price/100)
    total = total + price
print("shopping total", total/100)
```

### Conditional discount

Any item that costs more than £10 will be discounted by 20 percent. Use an `if` statement to check if the price is more than 1000 pennies.
If it is, multiply the price by 0.8 to reduce it before you add it to the total.

\newpage

Possible solution:

```python
prices = [349, 999, 250, 2000]
total = 0
for price in prices:
    print("item costs £", price/100)
    if price > 1000:
        price = price * 0.8
        print("  item discounted to", price/100)
    total = total + price
print("shopping total", total/100)
```

## Conditionals \& boolean logic

Only people older than 12 or taller than 150cm are allowed to ride the rollercoaster.  This program checks whether people are allowed to ride.

```python
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
if age > 12:
    print("You can ride")
elif height > 170:
    print("You can ride")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
```

Boolean operators combine two truth values together.  The `or` operator is `True` if either of its operands is true.  Try this example:

```python
a = True
b = False
print(a or b)
```

Now use the `or` operator to make the rollercoaster program shorter by combining the two tests into one test.

\newpage

A possible solution:

```python
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
if age > 12 or height > 170:
    print("You can ride")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
```

### And

The `and` operator is `True` if both of its operands is true.  Try this example:

```python
a = True
b = False
print(a and b)
```

The rollercoaster is only allowed to run on days when the temperature is less than 30 degrees.  Extend the program
to ask the temperature and use the `and` operator to only allow riding when less than 30 degrees.

\newpage

A possible solution:

```python
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
print("What is the temperature?")
temp = int(input())
if (age > 12 or height > 150) and temp < 30:
    print("You can ride")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
```

Note that we have put brackets around the `or` expression.  This ensures it is calculated first and the result of that calculation
is then used in the `and` expression.  This is the same way you use the BODMAS rule to decide the order of operations in maths.

### Not

The `not` operator is `True` if its operand is `False`.  If its operand is `False` then it is `True`.  Try this example:

```python
a = True
b = False
print(not a)
print(not b)
```



## Dictionaries

A dictionary (called a *HashMap* in some languages) stores pairs of values.  You can use the first value to look-up the second,
just like how you look-up a word in a dictionary to find its meaning.  Here is a dictionary of the ages of my friends:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
print("What is your name?")
name = input()
age = friends[name]
print("Your age is", age)
```

Change the program so it contains 5 of your friends' ages.


### Counting

Here is a loop that prints out all the ages:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
for name, age in friends.items():
    print(name, "is age", age)
```
    

Can you add an `if` statement to only print the ages of friends older than 10?

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
for name, age in friends.items():
    if age > 10:
        print(name, "is age", age)
```
        
Now add a `count` variable that counts how many of the friends are older than 10.  Print the number at the end.

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
count = 0
for name, age in friends.items():
    if age > 10:
        count = count + 1
print("friends older than 10:",count)
```

### Finding

We make a variable `oldest` that will contain the oldest age in the list.  

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
oldest = 0
for name, age in friends.items():
    if age > oldest:
        oldest = age
print("oldest age", oldest)
```

Now make a variable `youngest` that will contain the youngest age in the list.  Print the youngest at the end.

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
oldest = 0
youngest = 100
for name, age in friends.items():
    if age > oldest:
        oldest = age
    if age < youngest:
        youngest = age
print("oldest age", oldest)
print("youngest age", youngest)
```

### Finding names

As well as the ages, print the names of the youngest and oldest friends.

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
oldest = 0
youngest = 100
for name, age in friends.items():
    if age > oldest:
        oldest = age
        oldname = name
    if age < youngest:
        youngest = age
        youngname = name
print("oldest friend", oldname)
print("youngest friend", youngname)
```

### and

Use the `and` operator to only count friends between the ages of 11 to 13.

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
count = 0
for name, age in friends.items():
    if age > 10 and age < 14:
        count = count + 1
print("friends age 11 to 13 :",count)
```

### Find the average

Create a `total` variable.  Add each age to the total.  At the end, calculate the average by dividing the total by the number of
friends.

\newpage

Possible solution:

```python
friends = {'richard': 96, 'john': 12, 'paul': 8}
total = 0
for name, age in friends.items():
    total = total + age
average = total / 3
print("average age is ", average)
```

