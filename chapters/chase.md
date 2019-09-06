# Tutorial: Chase game

In this chapter we will build a complete chase game together, step by step.  The Python we will use is very simple: just conditionals and loops.

The techniques here should be familiar to you because we used them in Program~\ref{code:background}, \ref{code:keyboard_input}, \ref{code:collisions} and \ref{code:chase}

Now we will show you how to put them all together in one program.


## Moving Actor over a background

We must create two image files for our game.  You can use a program such as Krita FOOTNOOT to draw them and save them in the `images` folder (accessible with the
`images` button in Mu).  One is the player, called `player.png`.  It should be small, about 64×64 pixels.  Ideally it should have a transparent background.

The other is the background for the game itself.  It can look like whatever you want, but it must be the same size as the game window, which will be 600×600 pixels.

KRITA SCREENSHOT

\begin{codelisting}
\codecaption{Chase game}
\label{code:chase1}
<<(programs/chase1.py)
\end{codelisting}

* Run the program and move around

## Screen wrap-around

One problem you will soon find with the program is that you can move off the edge of the screen and get lost.  One way to solve this would be
to stop movement at the screen edges.  Instead we going to make the player teleport to the opposite edge when he leaves the screen.  Add this code
to the end of the program, and make sure it is indented so that it becomes part of the `update()` function.

```python
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0
```

* Change the code so that the player stops at the edges rather than wraps-around.
