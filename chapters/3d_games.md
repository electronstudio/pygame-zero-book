# 3D Games

The author has created a library similar to Pygame Zero but for creating 3d games: *richlib*. It is still experimental and subject to change.  The newest
version at time of writing is 0.0.6.

If you are using Mu then add the package ```richlib==0.0.6```

If you are using IDLE then type at the command line:

```python
pip3 install richlib==0.0.6
```

Richlib is similar to Pygame Zero, but there are some differences.

You now have to put

```python
run()
```

at the end of your programs.

This calls a method in Richlib. You can’t see it, but what it does is something like this:

```python
def run():
    while True:
        update()
        draw()
        time.sleep(0.1)
```

## Cubes and spheres

Much like Pygame draws rectangles and circles, Richlib draws cubes and spheres.  Note if using Mu you must be in `Python3` mode, not `Pygame Zero` mode.

\begin{codelisting}
\codecaption{Cubes and spheres}
\label{code:cubes}
<<(programs/rl_cubes_spheres.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Change the colors and positions of the cubes.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make sure you understand the 3d (x,y,z) co-ordinate system.
\end{aside}


## Moving cubes

Just like in Pygame, the `update()` function is called for us and is where we make things move.

\begin{codelisting}
\codecaption{Moving cubes}
\label{code:cubes}
<<(programs/rl_moving_cubes.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Make the box move faster.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make the box move in a different direction.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Make two different boxes with different colours.
\end{aside}


## Actors

Actors are similar to cubes but they load and display a complete 3d model.
The following 3d objects are currently built-in:

| barracks | bridge | castle | church | house |
| market | trooper | turret | watermill | well |

If you want any other objects you must provide an `.obj` 3d model file.

\begin{codelisting}
\codecaption{3d model actors}
\label{code:rl_actors}
<<(programs/rl_actors.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Change the `trooper` to one of the other 3d object build-ins listed above.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Try downloading some .obj files from the web.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Try to create an .obj file using https://www.leocad.org/ or https://www.blender.org/
\end{aside}

\pagebreak

## Keyboard input

\begin{codelisting}
\codecaption{Keyboard input}
\label{code:rl_keyboard_input}
<<(programs/rl_keyboard_input.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Make the alien move up and down as well as left and right when you press the arrow keys.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Use the `or` operator to allow the WASD keys to move the alien in addition to the arrow keys.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Make alien wrap around when he moves off the edge of the screen.
\end{aside}

## Controller input

Richlib has a game controller API that is a bit different from Pygame's.  This will require a game controller connected to work.

\begin{codelisting}
\codecaption{Game controller input}
\label{code:rl_joystick_input}
<<(programs/rl_joystick_input.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Make the alien move up/down and forward/back as well as left/right.
\end{aside}

## 3d collisions

\begin{codelisting}
\codecaption{3d collisions}
\label{code:rl_collisions}
<<(programs/rl_collisions.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Add vertical movement and if you have a controller make it work.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make the box move so that it chases the alien wherever he moves.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Print the number of times the box hits the alien (the score).
\end{aside}

\pagebreak

## Mouse input

We can get the mouse position in the 3d world and also test if mouse buttons are pressed.

\begin{codelisting}
\codecaption{Mouse input}
\label{code:rl_mouse}
<<(programs/rl_mouse.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Make the cube jump up when the mouse button is clicked.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make the cube change colour when the mouse button is held down.
\end{aside}


## Mouse collisions

We can check if the mouse pointer is touching a 3d object.

\begin{codelisting}
\codecaption{Mouse collisions}
\label{code:rl_mouse_collisions}
<<(programs/rl_mouse_collisions.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Increase the player's score each time he clicks on the cube.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make the cube get smaller each time he clicks on it.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent make it move to a random place after it is clicked on, e.g.
```python
                  import random
                  x = random.randint(0, 100)
```
\end{aside}

\pagebreak

## Sound effects

The `eep` sound is built-in.  Other sounds must be provided as `wav` files.  Click the mouse to play the sound.

\begin{codelisting}
\codecaption{Sound effects}
\label{code:rl_sounds}
<<(programs/rl_sounds.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Change the pitch each time the mouse is clicked.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Edit Program \ref{code:rl_mouse_collisions} so that it plays a sound when you hit the cube.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Record your own sound effect with the Audacity software and play it in your program.
\end{aside}

## Displaying text

Simple game where you press the space bar as fast as you can.  It displays score on screen.

Note that text is 2d, not 3d, so it must be drawn in `draw2d()` function not the normal `draw()` function.

\begin{codelisting}
\codecaption{Sound effects}
\label{code:rl_displaying_text}
<<(programs/rl_displaying_text.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent Make the score text larger and `RED` coloured.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Create a `score2` variable for player 2 that increases when P key is pressed and display it.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Add a score to one of your other programs and display it.
\end{aside}
