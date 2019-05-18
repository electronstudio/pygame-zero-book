# Drawing graphics

To create graphics for our games we will use [the Pygame Zero library](https://pygame-zero.readthedocs.io). You will find the documentation on the website useful!

If are using the Mu editor, Pygame Zero is built-in, but **you must remember to click 'Mode' and select 'Pygame Zero' before running your program!**

If you are using a different editor, [instructions are online](https://pygame-zero.readthedocs.io/en/stable/ide-mode.html)

## Lines and circles


\begin{codelisting}
\codecaption{Lines and circles}
\label{code:lines}
<<(programs/10_lines_circles.py)
\end{codelisting}

\noindent

Finishing drawing this picture, or your own picture.
Make sure you understand (x,y) co-ordinates
(In maths this called a 'Cartesian coordinate system'
and everything we do in Pygame Zero will use it)

## Getting input from the keyboard

When you run this program it will pause and wait for you to enter some
text with the keyboard, followed by the return key. The text you enter
is stored in a variable, *x*.

\begin{codelisting}
\codecaption{Getting input from the keyboard}
\label{code:input}
<<(programs/02_input.py)

\end{codelisting}

\noindent Can you add some names of your friends with different messages for each?

## Decisions: if, elif, else

This is how I added another name.

\begin{codelisting}
\codecaption{Decisions: if, elif, else}
\label{code:input2}
<<(programs/03_input2.py, options: "hl_lines": [6, 7, 8, 9])
\end{codelisting}

\noindent Program~\ref{code:input2} is very similar to Program~\ref{code:input}. The new lines have been highlighted.  You can either modify Program~\ref{code:input} or else create
a new file and use copy and paste to copy the code from the old program into the new.

## A random maths question

\begin{codelisting}
\codecaption{A random maths question}
\label{code:maths}
<<(programs/04_maths_question.py)
\end{codelisting}

* add some more questions, e.g.
   * instead of 7, use another random number
   * use a bigger random number
   * multiply or divide or subtract numbers
* print how many questions the player got correct at the end.

## Keeping score

\begin{codelisting}
\codecaption{Keeping score}
\label{code:maths2}
<<(programs/05_maths_question2.py)
\end{codelisting}

## Guessing game with a loop

\begin{codelisting}
\codecaption{Guessing game with a loop}
\label{code:loop}
<<(programs/06_loop.py)
\end{codelisting}

* give a hint to the player when they are wrong
* print how many guesses at the end

## Improved guessing game

\begin{codelisting}
\codecaption{Improved guessing game}
\label{code:loop2}
<<(programs/07_loop2.py)
\end{codelisting}