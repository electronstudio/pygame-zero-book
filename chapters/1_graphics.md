# Drawing graphics

To create graphics for our games we will use [the Pygame Zero library](https://pygame-zero.readthedocs.io). You will find the documentation on the website useful!

The smallest square that can be displayed on a monitor is called a *pixel*. This diagram shows a close-up view
of a window that is 40 pixels wide and 40 pixels high.  At normal size you will not see the grid lines.

![Model View Controller](images/figures/pixelgrid.pdf)

We can refer to any pixel by giving two co-ordinates, *(x,y)* Make sure you understand co-ordinates before moving on
because everything we do in Pygame Zero will use it.  (In maths this called a 'Cartesian coordinate system').

## Lines and circles

If are using the Mu editor, Pygame Zero is built-in, but **you must remember to click 'Mode' and select 'Pygame Zero' before running your program**!

If you are using a different editor, [instructions are online](https://pygame-zero.readthedocs.io/en/stable/ide-mode.html)

\begin{codelisting}
\codecaption{Lines and circles}
\label{code:lines_circles}
<<(programs/10_lines_circles.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Finish drawing this picture
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Draw your own picture.
\end{aside}
\newpage

## Moving rectangles

To make things move we need to add the special `update()` function.
We don't need to write our own loop because *Pygame Zero calls this function for us in its own loop*, over and over, many times per second.

\begin{codelisting}
\codecaption{Moving rectangles}
\label{code:moving_boxes}
<<(programs/11_moving_boxes.py)
\end{codelisting}


\begin{aside}
\label{}
\heading{}
\noindent Make the box move faster.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make the box move in different directions.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make two boxes with different colours.
\end{aside}

\newpage

## Actor sprites

Actor sprites are very similar to boxes!
Click `Images` to see the folder of image files available.
`alien.png` should already be there, but
for other images you must add the files yourself.

\begin{codelisting}
\codecaption{Actor sprites}
\label{code:sprites}
<<(programs/12_sprites.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Draw or download your own image to use instead of alien.  You could use Microsoft Paint which comes with Windows but
I recommend you download Krita from https://krita.org
\end{aside}

\newpage

## Background image

We are going to add a background image to  Program~\ref{code:sprites}

Click `Images` to see the folder of image files available.  

**You must create or download a picture
to use a background.  Save it as `background.png`.  It should be the same size as the window, 500×500 pixels.**

\begin{codelisting}
\codecaption{Background}
\label{code:background}
<<(programs/12b_background.py)
\end{codelisting}

\newpage

## Keyboard input

The alien moves when you press the cursor keys.

\begin{codelisting}
\codecaption{Keyboard input}
\label{code:keyboard_input}
<<(programs/13_keyboard_input.py)
\end{codelisting}


\begin{aside}
\label{}
\heading{}
\noindent Make the alien move up and down as well as left and right.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Use the more concise += operator to change the `alien.x` value (see Program~\ref{code:shortcuts}).
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent  Use the `or` operator to allow WASD keys to move the alien in addition to the cursor keys (see Program~\ref{code:logic}).
\end{aside}

\newpage

