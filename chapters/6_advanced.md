# Advanced topics


## Instructor note

This is the beginning of my attempts to teach object oriented programming, but I wouldn't attempt this with young students since it requires abstract thinking.



## Classes

You've already been using class types, e.g. Rect and Actor.
But if we want to store velocity as in Program~\ref{code:simple_physics} we find classes do not include *vx* and *vy* variables inside them.

There let's
create our own class, Sprite, that is the same as Actor but with
these variables included.

\begin{codelisting}
\codecaption{Classes}
\label{code:classes}
<<(programs/26_classes.py)
\end{codelisting}


\newpage


## Methods

Classes can contain functions (called *methods*) as well as variables.
Methods are the best place to modify the class's variables.

\begin{codelisting}
\codecaption{Class methods}
\label{code:classes2}
<<(programs/27_classes2.py)
\end{codelisting}


\newpage


## Joystick tester

This program demonstrates using joysticks and for loops, but is mainly included to help you test the input from your controllers.

(I don't suggest typing this one yourself.)

\begin{codelisting}
\codecaption{Joystick tester}
\label{code:joystick_tester}
<<(programs/19_joystick_tester.py)
\end{codelisting}

\newpage

## Distributing your Pygame Zero games

This is often tricky to get working, but you can distribute your games to people who don't have Python or Mu installed.  You can put them on a USB stick, or a website for people to download, or even on itch.io for people to buy.

1. Install the full version of python from [www.python.org](https://www.python.org/downloads/).

6. Edit your game source code (using Mu).  We will assume your source is in a file ```NAME_OF_GAME.py```.  At the top of the file add the line:
```python
import pgzrun
```
At the bottom of the file add the line:
```python
pgzrun.go()
```
Any time in the program you use `draw.text()` you *must* specify a font, e.g. add parameter  `fontname="arial"`

Save the file.

3. Copy any fonts you have used into the `fonts` folder and rename them to lowercase names, e.g. `arial.ttf`

3. Open a command prompt (Click start menu and type ```cmd.exe```)

4. Enter your mu_code folder.  At the prompt type:
    
    ```cd mu_code```
    
5. Install pyinstaller and pgzero.  At the command prompt type:

    ```pip install pgzero pyinstaller```
    
2. You should find the *pgzero* folder at:

    \verb+C:\Users\YOURNAME\AppData\\Local\\Programs\+

    \verb+Python\Python37\Lib\site-packages\pgzero+

    This is a hidden folder so you must enable hidden folders in Windows Explorer to see it.
    
    Copy the *pgzero* folder into your *mu_code* folder.
    
    You should find your *mu_code* folder at:
    \verb+C:\Users\YOURNAME\mu_code+
      
7. Create the executable.  At the command prompt type:
    
    ```pyinstaller NAME_OF_GAME.py --distpath . --add-data "pgzero;pgzero" --add-data "images;images" --add-data "fonts;fonts" "sounds;sounds" --add-data "music;music" --onefile --noconfirm --windowed --clean```
    
   This will generate a program called ```NAME_OF_GAME.exe```.  You can double click this program to play your game.
   
8. To distribute your game you need to copy the entire *mu_code* folder.  You could put it inside a zip file, and then
put that on a website

