# Python Fundamentals

There are some exercises here.  Each exercise will ask you to write a program.  The solution is
often on the following page - do not turn the page until you have attempted your own solution!  Save each program in a separate file.

* **Instructor note:** Unlike the rest of the book, these examples are not games.  For a 'fun' class, just discuss them, rather than having the students type them.
Also you can skip this chapter entirely and teach them only when they are relevant to one of the games, or use them to reinforce concepts from the games for students who need additional examples.
There are also some more formal exercises here
that you can use to evaluate students in a more academic setting.


\pagebreak

## The REPL

REPL stands for *Read Evaluate Print Loop*.  In Mu you access it via the `REPL` button.  It appears at the bottom of the window.  It's a special mode in which you type an instruction to Python and Python
executes it immediately (no need to click `RUN`) and displays the result (no need to type `print()`).  It's useful for doing calculations and trying things out, but it won't save what you type, so you will
only want to use it for very short programs.

![The REPL](images/figures/repl.png)

## Arithmetic operators

Python understands several operators from maths.  You can use them in your programs, or just enter these examples at the REPL to use Python as a calculator, as in the screenshot above.

| Operator | Symbol | Example | Result |
| ----- | ---- | ---- | ---- |
| Addition | + | 20 + 10 | 30 |
| Subtraction | - | 20 - 10 | 10 |
| Multiplication | * | 20 * 10 | 200 |
| Division | / | 20 / 10 | 2 |

There are some more advanced operators in Program~\ref{code:shortcuts}


## Variables

A *variable* is a place in the computer's memory where data is stored.  You can name a variable whatever you like; you should
try to make the name descriptive.  There are many *types* of variable but Python sets the type for us automatically
when we store data in the variable.  (Unlike in many other languages, we do not need to specify the type.)  The types we will see most
often are whole numbers (*integers*) and *strings* of text.

We create a variable and assign a value to it using the `=` operator.  Note this is different from the `==` operator which is used for comparisons.

We use the `print()` function to print the value of our variables.  It will print any type of data (numbers, strings, both literals and variables) provided each
item is separated with a comma (`,`). 

\begin{codelisting}
\codecaption{Variable assignment}
\label{code:variables}
```python
my_number = 7
my_string = "hello"
print(my_string, my_number)
```
\end{codelisting}

We can use a variable anywhere we would use a literal number or string.  The value of the variable will be retrieved from the computer's memory and substituted for the variable in any expression.

\begin{codelisting}
\codecaption{Adding two variables together}
\label{code:fruits}
```python
apples = 27
pears = 33
fruits = apples + pears
print("Number of fruits:", fruits)
```
\end{codelisting}

**Exercise:** Copy Program~\ref{code:fruits}, but also add 17 bananas to the calculation of fruits.

We can store a new value in the same variable.  The old value will be forgotten.

\begin{codelisting}
\codecaption{Overwriting a variable with a new value}
\label{code:overwriting}
```python
apples = 27
apples = 40
print("Number of apples:", apples)
```
\end{codelisting}

**Exercise:** What do you think Program~\ref{code:overwriting} will print?  If you aren't sure, type it in.


More usefully, we can take the old value, modify it, then store it back in the same variable.

\begin{codelisting}
\codecaption{Modifying a variable}
\label{code:mod_variables}
```python
x = 5
x = x * 10
x = x + 7
print(x)
```
\end{codelisting}

**Exercise:** What will Program~\ref{code:mod_variables} print?  Change the numbers in the program.  Use a division `/` operation.
Then ask your friend to predict what the new program will print.  Was he right?

You will often see this used for counting:

\begin{codelisting}
\codecaption{Counting}
\label{code:counting}
```python
total = 0
total = total + 1
total = total + 1
total = total + 1
print(x)
```
\end{codelisting}

**Exercise:** What is the total count of Program~\ref{code:counting} ?

See Program~\ref{code:shortcuts} for a quicker way of writing this.


## Input

Program~\ref{code:fruits} is not very useful if the number of apples changes.  This would require the programmer to change the program.  We can improve it by allowing the *user* of the program
to change the numbers.  The `input()` function allows the user to type a string which can be different every time the program is run.

```python
my_string = input()
print(my_string)
```

Sometimes we require that the user type in a number rather than a string.  We can use the `int()` function to convert the string to a number.

\begin{codelisting}
\codecaption{Getting input from user}
\label{code:input3}
```python
print("Enter a number")
my_number = int(input())
print("Double your number is", my_number * 2)
```
\end{codelisting}

**Exercise:** Copy Program~\ref{code:fruits} but use `input()` to ask the user to enter the number of apples and pears.



## Booleans

A *boolean* is a type of variable that is not a string or a number.  It can have only two possible values: `True` or `False`.  In some
languages and in electronics you may see these represented as `0` and `1`.

Booleans are used by keywords such as `if` and `while`.  In an `if` statement, the indented code block is only run if the boolean is
`True`.

```python
sunny = True
if a:
    print("Let's go to the park")
```

You could write it like this:
```python
sunny = True
if sunny==True:
    print("Yay!")
```
but that would be redundant because `if` always tests if the boolean is `True`.

If the boolean is not true, and if you write an `else` clause, the indented code block under `else` is run instead.
```python
sunny = False
if sunny:
    print("Let's go to the park")
else:
    print("We must stay at home")
```

## Boolean Logic

The `and`, `or` and `not` operators operate on booleans and return new boolean values.

\begin{codelisting}
\codecaption{Boolean logic}
\label{code:logic}
\phantom{.}
<<(programs/08_logic.py)
\end{codelisting}

not windy.

## Comparison operators

Comparison operators take two numbers, strings or other variables, compare them, and then return a *boolean* `True` or `False` from them.

| Operator | Symbol |
| ----- | ---- |
| Equal | == | 
| Not equal | != | 
| Less than | < | 
| Less than or equal | <= |
| Greater than | > |
| Greater than or equal | >= |

\begin{codelisting}
\codecaption{Comparisons: greater than, lesser than, equal to}
\label{code:logic2}
\phantom{.}
<<(programs/09_logic2.py)
\end{codelisting}

## Conditionals \& boolean logic

Only people older than 12 or taller than 150cm are allowed to ride the rollercoaster.  This program checks whether people are allowed to ride.

```python
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
if age > 12:
    print("You can ride")
elif height > 150:
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

**Exercise:** use the `or` operator to make the rollercoaster program shorter by combining the two tests into one test.

\newpage

A possible solution:

```python
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
if age > 12 or height > 150:
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

**Exercise:** The rollercoaster is only allowed to run on days when the temperature is less than 30 degrees.  Extend the program
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

We can get a user input and convert it to a boolean like this:

```python
print("Is it raining? Y/N")
if input() == "Y":
    raining = True
else:
    raining = False
```

**Exercise:** Change the program so that you can only ride the rollercoaster if it is not raining.

\newpage

Possible solution:

```python
print("Is it raining? Y/N")
if input() == "Y":
    raining = True
else:
    raining = False
print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
print("What is the temperature?")
temp = int(input())
if (age > 12 or height > 150) and temp < 30 and not raining:
    print("You can ride")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
```
 
## For loops
 
A `for` loop repeats a block of code a number of times.  A variable is created which we can use to find the current number within the loop.  Here
the variable is called `x` but you can name it whatever you like.  Run this program:
 
```python
 for x in range(0, 11):
     print(x)
```

You can also change the *step* of the loop.  Run this program:

```python
 for x in range(0, 11, 2):
     print(x)
```

### Nested loops

It is often useful to put one loop inside another loop. 

\begin{codelisting}
\codecaption{Nested for loop}
\label{code:for_loop}
```python
for a in range(0, 6):
    for b in range(0, 6):
        print(a, "times", b, "is", a * b)
```
\end{codelisting}

**Exercise:** write a program which prints out the 12 times table.
 
### Incrementing a variable in a loop
 
A baker has three customers.  He asks them each how many cakes they want
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
 
**Exercise**: This program is longer than it needs to be.  Instead of typing it, write your own program using a `for` loop.  It should be only 6 (or fewer) lines long.
 
\newpage
 
 
\begin{codelisting}
\codecaption{Possible solution to baker program exercise}
\label{code:baker}
```python
 total=0
 for x in range(1, 4):
     print("Customer", x, "how many cakes do you want?")
     cakes = int(input())
     total = total + cakes
 print("I will bake", total, "cakes!")
```
\end{codelisting}
 
**Exercise:** The baker gets a fourth customer.  Change Program~\ref{code:baker} so it works for 4 customers.
 
**Exercise:** The baker has a different number of customers every day.  Change the program so it
asks how many customers there are. Store the number typed by the user in a variable
called `c`. Change the loop so it works for `c` customers rather than 4 customers.
 
\newpage
 
\begin{codelisting}
\codecaption{Possible solution to variable number of customers exercise}
\label{code:baker2}
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
\end{codelisting}
 
**Exercise:** If a customer orders 12 cakes, he gets an extra cake for free.  Use an `if` statement to check `cakes > 12`. If so, add one more cake.



## Array lists

Variables can be stored together in a *list*. Most languages call this an *array* so try to remember that word also.[^afoot]
  
\begin{codelisting}
\codecaption{Array lists}
\label{code:arrays}
<<(programs/0C_arrays.py)
\end{codelisting}

[^afoot]: There are other kinds of list that are not arrays but this need not concern the beginner.

### Looping over lists


Rather than the user typing in data, your program might be supplied with data in a list.
Here is a list of prices  - a shopping list. Note we dont use a currency symbol except when we print the price.

```python
prices = [3.49, 9.99, 2.50, 20.00]
for x in range(0, 4):
    print("item costs £", prices[x])
```

In this program `x` is used an *index* for the array.  Note that indices begin at `0` rather than `1`.  If the array contains
4 elements then the final element witll have index `3`, nor `4`.

However, `for` can directly give you all the array values without
the need for an index or to specify the size of the range:

\begin{codelisting}
\codecaption{A shopping list}
\label{code:shoppinglist}
```python
prices = [3.49, 9.99, 2.50, 20.00]
for price in prices:
    print("item costs £", price)
```
\end{codelisting}

**Exercise:** Change the Program~\ref{code:shoppinglist} so that it prints the total price of all the items added together.

\newpage

\begin{codelisting}
\codecaption{Possible way of calculating the total cost of shopping list}
\label{code:shoppinglist2}
```python
prices = [3.49, 9.99, 2.50, 20.00]
total = 0
for price in prices:
    print("item costs £", price)
    total = total + price
print("shopping total", total)
```
\end{codelisting}

There is a problem with solution, can you see what it is when you run it?

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

\begin{codelisting}
\codecaption{Better way of calculating the total cost of shopping list}
\label{code:shoppinglist3}
```python
prices = [349, 999, 250, 2000]
total = 0
for price in prices:
    print("item costs £", price/100)
    total = total + price
print("shopping total", total/100)
```
\end{codelisting}

**Exercise:** Conditional discount.  Any item that costs more than £10 will be discounted by 20 percent. Use an `if` statement to check if the price is more than 1000 pennies.
If it is, multiply the price by 0.8 to reduce it before you add it to the total.

\newpage

\begin{codelisting}
\codecaption{Possible way of discounting shopping list}
\label{code:shoppinglist4}
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
\end{codelisting}

## Functions

You may have seen specially named functions that are called by Pygame: `draw()` and `update()`.
However, you can define a function named whatever you like and call it yourself.

Functions are useful for many reasons. The simplest is that they make your program look more organized. They also enable you re-use code without
needing to copy it and risk making mistakes.  When your programs get longer they enable you to create *abstractions* so you only have to think about
what function you want to call and don't need to remember the details of the code inside the function.

\begin{codelisting}
\codecaption{Functions}
\label{code:functions}
<<(programs/0D_functions.py)
\end{codelisting}

\pagebreak




## Shortcuts

Here are quicker ways of doing basic things.  You may have noticed some of these being used already.  

\begin{codelisting}
\codecaption{Shortcuts}
\label{code:shortcuts}
<<(programs/0A_shortcuts.py)
\end{codelisting}


\pagebreak

## Indentation

Code is arranged in *blocks*.  For example, a *function* consists of a one line delcaration followed by a block of several lines of code.  Similarly, all the lines
of a loop form one block.  A *conditional* has a block of code following the `if` statement (and optionally blocks after the `elif` and `else`. )

Many languages use `{}` or `()` to delimit a block.  However Python is unusual: each block begins with `:` and then all the lines of the block
are *indented* by the same amount of whitespace (tabs or spaces).  The block ends when the indentation ends.

Blocks can be *nested* inside other blocks.

\begin{codelisting}
\codecaption{Can you predict what this program will print?}
\label{code:blocks}
<<(programs/blocks.py)
\end{codelisting}

\pagebreak

## Global variables

A variable defined inside a function has *local scope*: it cannot be used outside of the function.  If you want to use the same
variable in different functions then you must define it outside the functions, in the *global scope*.  However, if you attempt to
modify the value of the global variable inside a function you will get an error, or - even worse - you will create a local variable with the same name as the global variable
and your changes to the global variable will be silently lost.

You must explicity tell Python that you
want to use a global variable with the `global` keyword.

\begin{codelisting}
\codecaption{Try removing line 3 and see what happens}
\label{code:globals}
```python
a = 10
def my_function():
    global a
    a=20
my_function()
print(a)
```
\end{codelisting}


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

### Combining tests

Use the `and` operator together with the `<` and `>` operators to only count friends between the ages of 11 to 13.

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




## Bugs

Fixing bugs can feel frustrating but all programmers must wrestle with them.  The simplest (but still annoying!) are *syntax errors*.
The computer is not very intelligent and is unable to guess what you mean, so you must type the programs in this book **exactly** as they appear.
A single wrong letter or space will prevent them from working.

A particular issue in Python is that *indentation* must be correct.

Can you spot and fix the bug in this program?

\begin{codelisting}
\codecaption{Buggy program}
\label{code:bug1}
<<(programs/0E_bug1.py)
\end{codelisting}

This one has two bugs to fix.

\begin{codelisting}
\codecaption{More bugs}
\label{code:bug2}
<<(programs/0F_bug2.py)
\end{codelisting}
