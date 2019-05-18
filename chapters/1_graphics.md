# Drawing graphics

To create graphics for our games we will use [the Pygame Zero library](https://pygame-zero.readthedocs.io). You will find the documentation on the website useful!

Co-ordinate diagram FIXME. Make sure you understand (x,y) co-ordinates(In maths this called a 'Cartesian coordinate system' and everything we do in Pygame Zero will use it)

## Lines and circles

If are using the Mu editor, Pygame Zero is built-in, but **you must remember to click 'Mode' and select 'Pygame Zero' before running your program**!

If you are using a different editor, [instructions are online](https://pygame-zero.readthedocs.io/en/stable/ide-mode.html)

\begin{codelisting}
\codecaption{Lines and circles}
\label{code:10_lines_circles}
<<(programs/10_lines_circles.py)
\end{codelisting}

* Finish drawing this picture, or your own picture.

\noindent\begin{minipage}{\textwidth}

## Moving rectangles

To make things move we need to add the special *update()* function.
Pygame Zero calls this function for us, over and over, once per frame.

\begin{codelisting}
\codecaption{Moving rectangles}
\label{code:11_moving_boxes}
<<(programs/11_moving_boxes.py)
\end{codelisting}

* Make box move faster.
* Move in different direction.
* Have two boxes with different colours.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Actor sprites

Actor sprites are very similiar to boxes!
Click 'Images' to see images available.
*alien.png* should already be there, but
for other images you must add them yourself.

\begin{codelisting}
\codecaption{Actor sprites}
\label{code:12_sprites}
<<(programs/12_sprites.py)
\end{codelisting}

* Draw or download your own image to use instead of alien.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Keyboard input

The alien moves when you press the cursor keys.

\begin{codelisting}
\codecaption{Keyboard input}
\label{code:13_keyboard_input}
<<(programs/13_keyboard_input.py)
\end{codelisting}

* Make the alien move up and down as well as left and right.
* Use the += operator to change the alien.x more concisely (see FIXME).
* Use the 'or' operator to allow WASD keys to move the alien in addition to the cursor keys (see FIXME).
* Make alien wrap around when he moves off edge of screen.

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Joystick input

You may call them gamepads or game controllers, but Pygame calls them joysticks.
 Some controllers have different inputs and some are not be compatible so don't be surprised if this doesnt work properly!  Use FIXME to test yours and find out what inputs it has.


\begin{codelisting}
\codecaption{Joystick input}
\label{code:14_joystick_input}
<<(programs/14_joystick_input.py)
\end{codelisting}

* Make the alien move up and down as well as left and right.

\vspace{\parskip}
\end{minipage}