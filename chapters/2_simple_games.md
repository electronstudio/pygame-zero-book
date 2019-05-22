# Aracade games

To 

\noindent\begin{minipage}{\textwidth}

## Collisions

Arcade games need to know when one sprite has hit another sprite.  Most of this code is copied from Program~\ref{code:moving_boxes} and Program~\ref{code:keyboard_input}.

\begin{codelisting}
\codecaption{Lines and circles}
\label{code:collisions}
<<(programs/15_collisions.py)
\end{codelisting}

* Joystick input (again), vertical movement (again).
* Make the box chase the alien.
* Print number of times hit (the score).

\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Sound and animation

Pygame Zero comes with one other image *alien_hurt.png* and one sound *eep.wav*.  If you want more you will have to add them to the *sounds* and *images* folders.

Most of this code is copied from Program~\ref{code:collisions} 

\begin{codelisting}
\codecaption{Sound and animation upon collision}
\label{code:collisions2_sound_animation}
<<(programs/16_collisions2_sound_animation.py)
\end{codelisting}

* Record your own sound effect
* Add more boxes or sprites that move in different ways to avoid
* Add a second alien controlled by different keys or gamepad

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Mouse clicks

This uses a function call-back for event-based input so you may want to explain functions. It is similiar to Program~\ref{code:collisions2_sound_animation} but

* box has been removed
* mouse function for clicking on alien
* score is displayed (FIXME)
  
\begin{codelisting}
\codecaption{Getting input from mouse clicks}
\label{code:mouse_input}
<<(programs/17_mouse_input.py)
\end{codelisting}

\vspace{\parskip}
\end{minipage}
\noindent\begin{minipage}{\textwidth}

## Mouse movement

If you are more interested in controllers than mice this may be skipped for now.  

\begin{codelisting}
\codecaption{Getting input from mouse movement}
\label{code:mouse_movement}
<<(programs/18_mouse_movement.py)
\end{codelisting}

* what happens if you delete line 8 and replace it with this:
```python
   animate(alien, pos=pos, duration=1, tween='bounce_end')
```
* what happens if you change on_mouse_move to on_mouse_down?
* can you make a game with one alien controlled by mouse
* and another controlled by keyboard?

\end{minipage}


