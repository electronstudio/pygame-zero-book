Improving your games
====================

Here are some tips that will enable you to enhance your games.



Joystick input
--------------

You may call them *gamepads* or *controllers*, but Pygame calls them
*joysticks*.

Some controllers have different inputs and some are not compatible at
all so don’t be surprised if this doesnt work properly! PS4 and Xbox One
controllers connected by USB cable seems to work best. Use
:numref:`code-joystick_tester` to test yours and find
out what inputs it has. Note: if you run this program with no controller
plugged in you will get an error.

.. literalinclude:: programs/14_joystick_input.py
   :caption: Joystick input
   :name: code-joystick_input
   :linenos:



.. topic:: Optional, if you have a controller

   Make the alien move up and down as well as left and right using the controller.  Do the same for any other examples that use the keyboard!


Colours
-------

Note that sometimes *colour* is spelt *color* in American programs.

Instead of using ready made colours like ‘red’, ‘yellow’, etc. you can
create your own color with a *tuple* of three numbers. The numbers must
be between 0 - 255 and represent how much *red*, *green* and *blue* to
mix together.

.. literalinclude:: programs/25_colours.py
   :caption: RGB colours
   :name: code-colours
   :linenos:



.. topic:: Advanced

   Change the green and blue amounts to make different colours.


.. topic:: Exercise

   Make a gray colour.


.. topic:: Advanced

   Make random colours.




Using loops
-----------

The loops from :numref:`code-loop` are useful for
graphical games too! Here we draw red circles using a *for loop*.

We draw green circles using a *loop within another loop*.

.. literalinclude:: programs/20_loops.py
   :caption: Loops are useful
   :name: code-loops
   :linenos:



.. topic:: Exercise

   `import random` at the top of the program and then make the positions random, e.g::

      x = random.randint(0, 100)



.. topic:: Advanced

    Learn about RGB colour and make random colours (see :numref:`code-colours`).


.. topic:: Advanced

   Create a timer variable and change colours based on time (see :numref:`code-timer`)


Fullscreen mode
---------------

Sometimes it is nice to play your game using the entire screen rather
than in a window. Add these lines to any game to enable fullscreen mode.
Then press *F* to go fullscreen, *ESCAPE* to quit.

.. literalinclude:: programs/26_fullscreen_mode.py
   :caption: Fullscreen mode
   :name: code-full_screen_mode
   :linenos:





Displaying the score
--------------------

This game shows how you can keep the score in a variable and print it on
to the game screen. You can display any other messages to the player the
same way.

.. literalinclude:: programs/27_displaying_text.py
   :caption: Keeping score in a variable and displaying it
   :name: code-displaying_text
   :linenos:



.. topic:: Exercise

    Make the score text larger.


.. topic:: Advanced

   Add a second player who presses a different key and show their score too.


.. topic:: Exercise

   Add text to one of your other games.

