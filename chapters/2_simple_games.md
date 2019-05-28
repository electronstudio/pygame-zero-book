# Arcade games

Now we can draw actor sprites to the screen we can begin to make simple arcade style games with them. 

\pagebreak

## Collisions

Arcade games need to know when one sprite has hit another sprite.  Most of this code is copied from Program~\ref{code:moving_boxes} and Program~\ref{code:keyboard_input}.

\begin{codelisting}
\codecaption{Lines and circles}
\label{code:collisions}
<<(programs/15_collisions.py)
\end{codelisting}

* Add joystick input (as before); add vertical movement (as before).
* Make the box chase the alien.
* Print number of times hit (the score).

\pagebreak

## Sound and animation

Pygame Zero comes with one other image `alien_hurt.png` and one sound `eep.wav`.  If you want more you will have to add them to the `sounds` and `images` folders.

Most of this code is copied from Program~\ref{code:collisions} 

\begin{codelisting}
\codecaption{Sound and animation upon collision}
\label{code:collisions2_sound_animation}
<<(programs/16_collisions2_sound_animation.py, options: "hl_lines": [19, 20, 21, 22, 23])
\end{codelisting}

* Record your own sound effect and add it to the game.
* Add more boxes or sprites that move in different ways for the player to avoid.
* Add a second alien controlled by different keys or gamepad for player 2.

\pagebreak

## Mouse clicks

This uses a *function call-back* for event-based input.  It is similiar to Program~\ref{code:collisions2_sound_animation} but:

* The box has been removed.
* There is an `on_mouse_down()` special function that is called automatically when the player click the mouse.
* The score is displayed.

\begin{aside}
\label{aside:mouseclicks}
\heading{Instructor note}
\noindent This is a good time to explain functions. See Program~\ref{code:functions} for more functions.
\end{aside}
  
\begin{codelisting}
\codecaption{Getting input from mouse clicks}
\label{code:mouse_input}
<<(programs/17_mouse_input.py)
\end{codelisting}

\pagebreak

## Mouse movement

If you are more interested in controllers than mice this may be skipped for now.  

\begin{codelisting}
\codecaption{Getting input from mouse movement}
\label{code:mouse_movement}
<<(programs/18_mouse_movement.py)
\end{codelisting}

* What happens if you delete line 8 and replace it with this:
```python
   animate(alien, pos=pos, duration=1, tween='bounce_end')
```
* What happens if you change `on_mouse_move` to `on_mouse_down`?
* Can you make a game with one alien controlled by mouse and another controlled by keyboard?




