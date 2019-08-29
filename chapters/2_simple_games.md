# Arcade games

Now we can draw actor sprites to the screen, we can begin to make simple arcade games with them. 

\newpage

## Collisions

Arcade games need to know when one actor sprite has hit another actor sprite.  Most of this code is copied from Program~\ref{code:moving_boxes} and Program~\ref{code:keyboard_input}.

\begin{codelisting}
\codecaption{Collisions}
\label{code:collisions}
<<(programs/15_collisions.py)
\end{codelisting}

* Add joystick input (as before); add vertical movement (as before).
* Make the box chase the alien.
* Print number of times hit (the score).

\pagebreak

## Chase

Instead of moving constantly to the right we can make the movement conditional with an `if` statement so the box chases the alien.
Most of this code is copied from Program~\ref{code:collisions}.  New lines are heighlighted.  We have also changed what happens when the box
catches the alien: the program now exits and you must run it again to play again.  This may not be what you want in your game!

\begin{codelisting}
\codecaption{Alien chase}
\label{code:chase}
<<(programs/15b_chase.py, options: "hl_lines": [17, 18, 19, 20, 21, 22])
\end{codelisting}

* Add joystick input (as before); add vertical movement (as before).
* Draw a new enemy image.  Save it as `enemy.png` in your `mu_code/images` folder. Load it as an `Actor('enemy')` instead of the `Rect()`.

\pagebreak

## Powerup

Instead of an enemy the box here is a powerup that the player must collect.  When he does it disappears and moves to a new location.

\begin{codelisting}
\codecaption{Collect the powerups}
\label{code:powerup}
<<(programs/15c_powerup.py)
\end{codelisting}

* Add joystick input (as before); add vertical movement (as before).
* Draw a new enemy image.  Save it as `powerup.png` in your `mu_code/images` folder. Load it as an `Actor('powerup')` instead of the `Rect()`.
* Combine this program with the enemy from  Program~\ref{code:chase}, the background from  Program~\ref{code:background} to make your game.

\pagebreak

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

If you are more interested in playing using controllers than mice this may be skipped for now.  

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




