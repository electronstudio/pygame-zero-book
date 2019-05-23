# More games

FIXME

\noindent\begin{minipage}{\textwidth}

## Array lists

We introduced arrays in FIXME.  Create an empty array, use a loop to fill it with aliens
Draw the aliens, move the aliens
Add a new alien when the mouse is clicked.

\begin{codelisting}
\codecaption{Array lists are useful in games!}
\label{code:shortcuts}
<<(programs/0A_shortcuts.py)
\end{codelisting}

* Go back to your previous game (e.g. FIXME6)
  make an array of bullets that shoot when you
  press the space bar

\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Animation

This is another use for functions. (See FIXME)  We define our own function and then ask Pygame to call it
every 0.2 seconds.

\begin{codelisting}
\codecaption{Animation}
\label{code:animation}
<<(programs/22_animation.py)
\end{codelisting}

* make the alien animate faster
* add another image to list of images
* draw your own animation, e.g. a man walking left and make it play when the left key is pressed

\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Simple physics

Make a ball that bounces using simple velocity vector (vx and vy)
  
\begin{codelisting}
\codecaption{Simple physics: velocity}
\label{code:simple_physics}
<<(programs/23_simple_physics.py)
\end{codelisting}

* Make the ball get faster each time it hits the sides

\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Pong

Classic bat and ball game 

\begin{codelisting}
\codecaption{Pong}
\label{code:pong}
<<(programs/24_pong.py)
\end{codelisting}

* Add another bat at the top of the screen for player 2
* Add bricks (Rects) that disappear when the ball hits them

\end{minipage}

\noindent\begin{minipage}{\textwidth}

## Timer

Pygame can tell us how much time has passed since the last frame
in a parameter to our update function. We use this to keep a timer.

\begin{codelisting}
\codecaption{Timer}
\label{code:timer}
<<(programs/28_timer.py)
\end{codelisting}

This one has two bugs to fix.

\end{minipage}

\noindent\begin{minipage}{\textwidth}

## Another timer

Pygame can tell us how much time has passed since the last frame
in a parameter to our update function. We use this to keep a timer.

\begin{codelisting}
\codecaption{Timer with callback functions}
\label{code:timer2}
<<(programs/29_timer2.py)
\end{codelisting}

* Make the aliens appear much faster
* Use len(aliens) to print how many aliens there are
* When there are too many aliens, stop adding them using this code:

    clock.unschedule(add_alien)

\end{minipage}