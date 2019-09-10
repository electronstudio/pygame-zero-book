# Text-based quiz games

These programs can be entered using any text editor, but I suggest using [the Mu editor](https://codewith.mu/)
because it comes with Python, Pygame Zero and other libraries all pre-installed in one easy download.

## Hello, world

The traditional first program used to make sure Python is working and that we can run programs. 

\begin{codelisting}
\codecaption{Hello, world}
\label{code:hello}
<<(programs/01_intro.py)
\end{codelisting}

\noindent If using the Mu editor:

1. Click the mode button and make sure the mode is set to `Python3`.
2. Type in the program. 
3. Click `Save` and enter a name for the program.
4.  Click `Run`.

## Getting input from the keyboard

This program will pause and wait for you to enter some
text with the keyboard, followed by the return key. The text you enter
is stored in a variable, `x`.

\begin{codelisting}
\codecaption{Getting input from the keyboard}
\label{code:input}
<<(programs/02_input.py)

\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Add some names of your friends and display a different message for each friend.
\end{aside}


## Making decisions: if, elif, else

This is how to add another name to Program~\ref{code:input}

\begin{codelisting}
\codecaption{Decisions: if, elif, else}
\label{code:input2}
<<(programs/03_input2.py, options: "hl_lines": [6, 7, 8, 9])
\end{codelisting}

\noindent Program~\ref{code:input2} is very similar to Program~\ref{code:input}. The new lines have been highlighted.  You can either modify Program~\ref{code:input}, or else create
a new file and use copy and paste to copy the code from the old program into the new.

## A random maths question

\begin{codelisting}
\codecaption{A random maths question}
\label{code:maths}
\phantom{.}
<<(programs/04_maths_question.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Add some more questions, e.g.

* Instead of 7, use another random number.
* Use a bigger random number.
* Multiply (use `*`), divide (use `/`) or subtract (use `-`) numbers.

\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Print how many questions the player got correct at the end.
\end{aside}


\newpage

## Keeping score

We create a `score` variable to record how many questions the player answered correctly.

\begin{codelisting}
\codecaption{Keeping score}
\label{code:maths2}
\phantom{.}
<<(programs/05_maths_question2.py)
\end{codelisting}

\newpage

## Guessing game with a loop
 
This `while` loop goes round and round forever ... or until the player gets a correct
answer, and then it `break`s out of the loop.  Note that everything in the loop is indented.
 
\begin{codelisting}
\codecaption{Guessing game with a loop}
\label{code:loop}
\phantom{.}
<<(programs/06_loop.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Give a hint to the player when they are wrong.  Was their guess too high or too low?
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Print how many guesses they took to get it right at the end.
\end{aside}

\newpage

## Improved guessing game

Program~\ref{code:loop} with a hint whether the guess is greater or lesser than the answer.

\begin{codelisting}
\codecaption{Improved guessing game}
\label{code:loop2}
\phantom{.}
<<(programs/07_loop2.py)
\end{codelisting}


