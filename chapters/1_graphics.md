# Drawing graphics

To create graphics for our games we will use [the Pygame Zero library](https://pygame-zero.readthedocs.io). You will find the documentation on the website useful!

The smallest square that can be displayed on a monitor is called a *pixel*. This diagram shows a close-up view
of a window that is 40 pixels wide and 40 pixels high.  At normal size you will not see the grid lines.

![Model View Controller](images/figures/pixelgrid.pdf)

We can refer to any pixel by giving two co-ordinates, *(x,y)* Make sure you understand co-ordinates before moving on
because everything we do in Pygame Zero will use it.  (In maths this called a 'Cartesian coordinate system').

\vspace{20mm}

\noindent\begin{minipage}{\textwidth}

## Lines and circles

If are using the Mu editor, Pygame Zero is built-in, but **you must remember to click 'Mode' and select 'Pygame Zero' before running your program**!

If you are using a different editor, [instructions are online](https://pygame-zero.readthedocs.io/en/stable/ide-mode.html)

\begin{codelisting}
\codecaption{Lines and circles}
\label{code:lines_circles}
<<(programs/10_lines_circles.py)
\end{codelisting}

* Finish drawing this picture, or your own picture.

\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Moving rectangles

To make things move we need to add the special `update()` function.
We don't need to write our own loop because *Pygame Zero calls this function for us in its own loop*, over and over, many times per second.

\begin{codelisting}
\codecaption{Moving rectangles}
\label{code:moving_boxes}
<<(programs/11_moving_boxes.py)
\end{codelisting}

* Make the box move faster
* and in different directions.
* Make two boxes with different colours.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Actor sprites

Actor sprites are very similar to boxes!
Click `Images` to see the folder of image files available.
`alien.png` should already be there, but
for other images you must add the files yourself.

\begin{codelisting}
\codecaption{Actor sprites}
\label{code:prites}
<<(programs/12_sprites.py)
\end{codelisting}

* Draw or download your own image to use instead of alien.  You could use Microsoft Paint which comes with Windows.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Keyboard input

The alien moves when you press the cursor keys.

\begin{codelisting}
\codecaption{Keyboard input}
\label{code:keyboard_input}
<<(programs/13_keyboard_input.py)
\end{codelisting}

* Make the alien move up and down as well as left and right.
* Use the += operator to change the alien.x more concisely (see Program~\ref{code:shortcuts}).
* Use the `or` operator to allow WASD keys to move the alien in addition to the cursor keys (see Program~\ref{code:logic}).
* Make alien wrap around when he moves off edge of screen.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Joystick input

You may call them *gamepads* or game *controllers*, but Pygame calls them *joysticks*.

 Some controllers have different inputs and some are not compatible at all so don't be surprised if this doesnt work properly!  PS4 and Xbox One controllers connected by USB cable seems to work best.  Use Program~\ref{code:joystick_tester} to test yours and find out what inputs it has.  Note that if you come back to this program in future when you no longer have a controller plugged in you will get an error.


\begin{codelisting}
\codecaption{Joystick input}
\label{code:oystick_input}
<<(programs/14_joystick_input.py)
\end{codelisting}

* Make the alien move up and down as well as left and right.

\end{minipage}