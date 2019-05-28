# More graphics

Here are some tips that will enable you to enhance your games.

\newpage

## Using loops

The loops from Program~\ref{code:loop} are useful for something!  We draw red circles using a *for loop*.

We draw greeen circles using a loop within another loop.

\begin{codelisting}
\codecaption{Loops are useful}
\label{code:loops}
<<(programs/20_loops.py)
\end{codelisting}

* `import random` and make the positions random, e.g. use
```
random.randint(0, 100)
```
* Learn about RGB colour and make random colours (see Program~\ref{code:colours}).

* Create a timer variable and change colours based on time (see Program~\ref{code:timer})

\pagebreak

## Colours

Note that sometimes *colour* is spelt *color* in American programs.

Instead of using ready made colours like 'red', 'yellow', etc. you can create your
own color from three numbers. The numbers must be between 0 - 255 and represent
how much *red*, *green* and *blue* to mix together.


\begin{codelisting}
\codecaption{RGB Colours}
\label{code:colours}
<<(programs/25_colours.py)
\end{codelisting}

* Change the green and blue amounts to make different colours
* Can you make gray?
* Make random colours

\pagebreak

## Fullscreen mode

Sometimes it is nice to play your game using the entire screen rather than in a window.
Add these lines to any game to enable fullscreen mode.
Then press *F* to go fullscreen, *ESCAPE* to quit.
  
\begin{codelisting}
\codecaption{Fullscreen mode}
\label{code:full_screen_mode}
<<(programs/26_fullscreen_mode.py)
\end{codelisting}

\pagebreak

## Displaying the score

This game shows how you can keep the score in a variable and print it on to the game screen.  You can print any other
messages to the player the same way.

\begin{codelisting}
\codecaption{Keeping score}
\label{code:displaying_text}
<<(programs/27_displaying_text.py)
\end{codelisting}

* Make the score text larger.
* Add a second player who presses a different key and show their score too.
* Add text to one of your other games.




