# Improving your games

Here are some tips that will enable you to enhance your games.

\newpage

## Joystick input

You may call them *gamepads* or *controllers*, but Pygame calls them *joysticks*.

Some controllers have different inputs and some are not compatible at all so don't be surprised if this doesnt work properly!  PS4 and Xbox One controllers connected by USB cable seems to work best.  Use Program~\ref{code:joystick_tester} to test yours and find out what inputs it has.  Note: if you run this program with no controller plugged in you will get an error.


\begin{codelisting}
\codecaption{Joystick input}
\label{code:joystick_input}
<<(programs/14_joystick_input.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{Optional, if you have a controller}
\noindent Make the alien move up and down as well as left and right using the controller.  Do the same for any other examples that use the keyboard!
\end{aside}



## Colours

Note that sometimes *colour* is spelt *color* in American programs.

Instead of using ready made colours like 'red', 'yellow', etc. you can create your
own color with a *tuple* of three numbers. The numbers must be between 0 - 255 and represent
how much *red*, *green* and *blue* to mix together.


\begin{codelisting}
\codecaption{RGB colours}
\label{code:colours}
<<(programs/25_colours.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Change the green and blue amounts to make different colours.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Make a gray colour.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Make random colours.
\end{aside}

\pagebreak


## Using loops

The loops from Program~\ref{code:loop} are useful for graphical games too!  Here we draw red circles using a *for loop*.

We draw green circles using a *loop within another loop*.

\begin{codelisting}
\codecaption{Loops are useful}
\label{code:loops}
<<(programs/20_loops.py)
\end{codelisting}


\begin{aside}
\label{}
\heading{}
\noindent `import random` at the top of the program and then make the positions random, e.g.
```
x = random.randint(0, 100)
```
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent  Learn about RGB colour and make random colours (see Program~\ref{code:colours}).
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Create a timer variable and change colours based on time (see Program~\ref{code:timer})
\end{aside}





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

This game shows how you can keep the score in a variable and print it on to the game screen.  You can display any other
messages to the player the same way.

\begin{codelisting}
\codecaption{Keeping score in a variable and displaying it}
\label{code:displaying_text}
<<(programs/27_displaying_text.py)
\end{codelisting}

\begin{aside}
\label{}
\heading{}
\noindent  Make the score text larger.
\end{aside}

\begin{aside}
\label{}
\heading{Advanced}
\noindent Add a second player who presses a different key and show their score too.
\end{aside}

\begin{aside}
\label{}
\heading{}
\noindent Add text to one of your other games.
\end{aside}




