# Python Fundamentals

Now we've had some fun with games I hope to have generated enough interest to tackle some coding basics!

\begin{aside}
\label{aside:funda}
\heading{Instructor note}
\noindent Unlike the rest of the book, these examples are not games.  For a 'fun' class, just discuss them, rather than having the students type them.
Also you can skip this chapter entirely and teach them only when they are relevant to one of the games, or use them to reinforce concepts from the games for students who need additional examples.
There are also some more formal exercises here
that you can use to evaluate students in a more academic setting.
\end{aside}

\pagebreak

## The REPL

REPL stands for *Read Evaluate Print Loop*.  In Mu you access it via the `REPL` button.  It appears at the bottom of the window.  It's a special mode in which you type an instruction to Python and Python
executes it immediately (no need to click `RUN`) and displays the result (no need to type `print()`).  It's useful for doing calculations and trying things out, but it won't save what you type, so you will
only want to use it for very short programs.

![The REPL](images/figures/repl.png)

## Variables

A *variable* is a place in the computer's memory where data is stored.  You can name a variable whatever you like; you should
try to make the name descriptive.  There are many *types* of variable but Python sets the type for us automatically
when we store data in the variable.  (Unlike in many other languages, we do not need to specify the type.)  The types we will see most
often are whole numbers (*integers*) and *strings* of text.

We create a variable and assign a value to it using the `=` operator.  Note this is different from the `==` operator which is used for comparisons.

We use the `print()` function to print the value of our variables.  It will print any type of data (e.g. numbers, strings, literals) provided each
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

**Exercise:** Copy Program~\ref{code:fruits} but also add 17 bananas to the calculation.

## Input

## Logic

\begin{codelisting}
\codecaption{Boolean logic}
\label{code:logic}
\phantom{.}
<<(programs/08_logic.py)
\end{codelisting}

## Comparisons

\begin{codelisting}
\codecaption{Comparisons: greater than, lesser than, equal to}
\label{code:logic2}
\phantom{.}
<<(programs/09_logic2.py)
\end{codelisting}

\pagebreak

## Shortcuts

Shortcuts are quicker ways of doing basic things.  You may have noticed some of these being used already.  

\begin{codelisting}
\codecaption{Shortcuts}
\label{code:shortcuts}
<<(programs/0A_shortcuts.py)
\end{codelisting}


\pagebreak

## For loops

It is often useful to put one loop inside another loop. 

\begin{codelisting}
\codecaption{Times tables with for loops}
\label{code:for_loop}
<<(programs/0B_for_loop.py)
\end{codelisting}

* Can you print 12 times table?


## Array lists

Variables can be stored together in a *list*. Most languages call this an *array* so try to remember that word also.[^afoot]
  
\begin{codelisting}
\codecaption{Array lists}
\label{code:arrays}
<<(programs/0C_arrays.py)
\end{codelisting}

[^afoot]: There are other kinds of list that are not arrays but this need not concern the beginner.



## Functions

You have already defined specially named functions that are called by Pygame: `draw()` and `update()`.
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
