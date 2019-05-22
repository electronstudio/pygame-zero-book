# Python Fundamentals

Now we've had some fun with games I hope to have generated enough interest to tackle some coding basics.  I don't have the students type these, just discuss them, and possibly not all in the same lesson.

\noindent\begin{minipage}{\textwidth}

## Shortcuts

You may have noticed some of these being used already.  They are quicker ways of doing basic things.

\begin{codelisting}
\codecaption{Shortcuts}
\label{code:shortcuts}
<<(programs/0A_shortcuts.py)
\end{codelisting}


\end{minipage}
\noindent\begin{minipage}{\textwidth}

## For loops

It is often useful to put one loop inside another loop. 

\begin{codelisting}
\codecaption{Times tables with for loops}
\label{code:for_loop}
<<(programs/0B_for_loop.py)
\end{codelisting}

* Can you print 12 times table?

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Arrays

Python calls them *lists* but most languages call them arrays.
  
\begin{codelisting}
\codecaption{Array lists}
\label{code:arrays}
<<(programs/0C_arrays.py)
\end{codelisting}

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Functions

You have already defined specially named functions that are called by Pygame: *draw()* and *update()*
However you can define a function named whatever you like and call it yourself.

Functions are useful for many reasons. The simplest is that they make your program look more organized. They also enable you re-use code without
needing to copy it and risk making mistakes.  

\begin{codelisting}
\codecaption{Functions}
\label{code:functions}
<<(programs/0D_functions.py)
\end{codelisting}

\end{minipage}

\noindent\begin{minipage}{\textwidth}

## Bugs

Fixing bugs can feel frustrating but all programmers must wrestle with them.  Can you spot and fix the bug in this program?

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

\end{minipage}