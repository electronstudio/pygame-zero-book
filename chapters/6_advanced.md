# Advanced topics
\begin{aside}
\label{aside:advanced}
\heading{Instructor note}

\noindent This is beginning of my attempts to teach object oriented programming, but I wouldn't attempt this with young students.

\end{aside}




\noindent\begin{minipage}{\textwidth}

## Classes

You've already been using class types, e.g. Rect and Actor.
But if we want to store velocity as in Program~\ref{code:simple_physics} we find classes do not include *vx* and *vy* variables inside them.

There let's
create our own class, Sprite, that is the same as Actor but with
these variables included.

\begin{codelisting}
\codecaption{Classes}
\label{code:classes}
<<(programs/26_classes.py)
\end{codelisting}

\end{minipage}
\vspace{\parskip}
\newpage
\noindent\begin{minipage}{\textwidth}

## Methods

Classes can contain functions (called *methods*) as well as variables.
Methods are the best place to modify the class's variables.

\begin{codelisting}
\codecaption{Class methods}
\label{code:classes2}
<<(programs/27_classes2.py)
\end{codelisting}

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Joystick tester

This is an example of controller input and example of for loops but
mostly here so you can test your controllers' input.
I dont's suggest typing this one yourself.

\begin{codelisting}
\codecaption{Joystick tester}
\label{code:joystick_tester}
<<(programs/19_joystick_tester.py)
\end{codelisting}

\vspace{\parskip}
\end{minipage}
