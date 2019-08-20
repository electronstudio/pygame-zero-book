# More games

These games demonstrate some essential building blocks you will need to make more advanced games of your own.

\newpage

## Lists

We introduced lists in Program~\ref{code:arrays}.

In this game, we create an empty list *[]* and use a loop to fill it with aliens.

We again use loops to draw all the aliens and move all the aliens in the list.

When the mouse is clicked we add a new alien to the list.

\begin{codelisting}
\codecaption{Lists are useful in games!}
\label{code:arrays2}
<<(programs/21_arrays.py)
\end{codelisting}

* Go back to a previous game (e.g. Program~\ref{code:collisions})
  and add a list of bullets that move up the screen.  When the player presses the spacebar to shoot,
  add a new bullet to the list.

\pagebreak

## Animation

Animation is another use for functions. (See Program~\ref{code:functions})  We define our own function and then ask Pygame to *call it back*
every 0.2 seconds.
Most of this code is from Program~\ref{code:collisions}.

\begin{codelisting}
\codecaption{Animation}
\label{code:animation}
<<(programs/22_animation.py)
\end{codelisting}

* Make the alien animate faster.
* Add another image to the list of images.
* Draw your own animation, e.g. a man walking left which plays when the left key is pressed

\pagebreak

## Simple physics

Here we draw a ball and move it, like we did in Program~\ref{code:moving_boxes}.  But instead of moving it by a fixed number of pixels, we store the number of pixels to move in variables, `vx` and `vy`.
These are *velocities*, i.e. speed in a fixed direction.  `vx` is the speed in the horizontal direction and `vy` is the speed in the vertical direction.
This allow us to change the velocity.  Here we reverse the velocity when the ball hits the edge of the screen.
  
\begin{codelisting}
\codecaption{Simple physics: velocity}
\label{code:simple_physics}
<<(programs/23_simple_physics.py)
\end{codelisting}

* Make the ball move faster by increasing its velocity each time it hits the sides.

\pagebreak

## Bat and ball game

*Pong* is the classic bat and ball game.

\begin{codelisting}
\codecaption{Pong}
\label{code:pong}
<<(programs/24_pong.py)
\end{codelisting}

* Make the ball move more quickly.
* Add another bat at the top of the screen for player 2.
* Add bricks (Rects) that disappear when the ball hits them.

\pagebreak

## Timer

The `update()` and `draw()` functions are called by Pygame many times every second.  Each time `draw()` is called we say it draws one *frame*.
The exact number of frames per second is called the *framerate* and
it will vary from one computer to another.  Therefore counting frames is not very useful for timing.

Fortunately Pygame can tell us exactly how much many seconds have passed since the last frame
in a parameter to our update function. We use this *delta time* to keep a timer.

\begin{codelisting}
\codecaption{Timer}
\label{code:timer}
<<(programs/28_timer.py)
\end{codelisting}

* Make the timer count down, not up.
* Add a timer to one of your other games.
* Add a timer to Program~\ref{code:arrays} that deletes one of the aliens when the timer runs out, then starts the timer again.

\pagebreak

## Callbacks: another kind of timer

Pygame has its own clock which we can use by asking it to *callback* one of our
functions at a certain time, or regularly over and over at an interval.

\begin{codelisting}
\codecaption{Timer with callback functions}
\label{code:timer2}
<<(programs/29_timer2.py)
\end{codelisting}

* Make the aliens appear much faster
* Use ```len(aliens)``` to print how many aliens there are
* When there are too many aliens, stop adding them using this code:
```python
    clock.unschedule(add_alien)
```
