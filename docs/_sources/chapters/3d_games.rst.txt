3D Games
========

The author has created a library similar to Pygame Zero but for creating
3d games: *richlib*. It is still experimental and subject to change. The
newest version at time of writing is 0.0.6.

If you are using Mu then add the package ``richlib==0.0.6``

If you are using IDLE then type at the command line:

.. code:: python

   pip3 install richlib==0.0.6

Richlib is similar to Pygame Zero, but there are some differences.

You now have to put

.. code:: python

   run()

at the end of your programs.

This calls a method in Richlib. You can’t see it, but what it does is
something like this:

.. code:: python

   def run():
       while True:
           update()
           draw()
           time.sleep(0.1)

Cubes and spheres
-----------------

Much like Pygame draws rectangles and circles, Richlib draws cubes and
spheres. Note if using Mu you must be in ``Python3`` mode, not
``Pygame Zero`` mode.

.. literalinclude:: programs/rl_cubes_spheres.py
   :caption: Cubes and spheres
   :name: code-cubes
   :linenos:



.. topic:: Exercise

   Change the colors and positions of the cubes.


.. topic:: Exercise

   Make sure you understand the 3d (x,y,z) co-ordinate system.


Moving cubes
------------

Just like in Pygame, the ``update()`` function is called for us and is
where we make things move.

.. literalinclude:: programs/rl_moving_cubes.py
   :caption: Moving cubes
   :name: code-cubes
   :linenos:



.. topic:: Exercise

   Make the box move faster.


.. topic:: Exercise

   Make the box move in a different direction.


.. topic:: Advanced

   Make two different boxes with different colours.


Actors
------

Actors are similar to cubes but they load and display a complete 3d
model. The following 3d objects are currently built-in:

| barracks \| bridge \| castle \| church \| house \|
| market \| trooper \| turret \| watermill \| well \|

If you want any other objects you must provide an ``.obj`` 3d model
file.

.. literalinclude:: programs/rl_actors.py
   :caption: 3d model actors
   :name: code-rl_actors
   :linenos:



.. topic:: Exercise

   Change the `trooper` to one of the other 3d object build-ins listed above.


.. topic:: Advanced

   Try downloading some .obj files from the web.


.. topic:: Advanced

   Try to create an .obj file using https://www.leocad.org/ or https://www.blender.org/




Keyboard input
--------------

.. literalinclude:: programs/rl_keyboard_input.py
   :caption: Keyboard input
   :name: code-rl_keyboard_input
   :linenos:



.. topic:: Exercise

   Make the alien move up and down as well as left and right when you press the arrow keys.


.. topic:: Exercise

   Use the `or` operator to allow the WASD keys to move the alien in addition to the arrow keys.


.. topic:: Advanced

   Make alien wrap around when he moves off the edge of the screen.


Controller input
----------------

Richlib has a game controller API that is a bit different from Pygame’s.
This will require a game controller connected to work.

.. literalinclude:: programs/rl_joystick_input.py
   :caption: Game controller input
   :name: code-rl_joystick_input
   :linenos:



.. topic:: Exercise

   Make the alien move up/down and forward/back as well as left/right.


3d collisions
-------------

.. literalinclude:: programs/rl_collisions.py
   :caption: 3d collisions
   :name: code-rl_collisions
   :linenos:



.. topic:: Exercise

   Add vertical movement and if you have a controller make it work.


.. topic:: Exercise

   Make the box move so that it chases the alien wherever he moves.


.. topic:: Advanced

   Print the number of times the box hits the alien (the score).




Mouse input
-----------

We can get the mouse position in the 3d world and also test if mouse
buttons are pressed.

.. literalinclude:: programs/rl_mouse.py
   :caption: Mouse input
   :name: code-rl_mouse
   :linenos:



.. topic:: Exercise

   Make the cube jump up when the mouse button is clicked.


.. topic:: Exercise

   Make the cube change colour when the mouse button is held down.


Mouse collisions
----------------

We can check if the mouse pointer is touching a 3d object.

.. literalinclude:: programs/rl_mouse_collisions.py
   :caption: Mouse collisions
   :name: code-rl_mouse_collisions
   :linenos:



.. topic:: Exercise

   Increase the player's score each time he clicks on the cube.


.. topic:: Exercise

   Make the cube get smaller each time he clicks on it.


.. topic:: Advanced

   make it move to a random place after it is clicked on, e.g.::

      import random
      x = random.randint(0, 100)





Sound effects
-------------

The ``eep`` sound is built-in. Other sounds must be provided as ``wav``
files. Click the mouse to play the sound.

.. literalinclude:: programs/rl_sounds.py
   :caption: Sound effects
   :name: code-rl_sounds
   :linenos:



.. topic:: Exercise

   Change the pitch each time the mouse is clicked.


.. topic:: Exercise

   Edit Program \ref{code:rl_mouse_collisions} so that it plays a sound when you hit the cube.


.. topic:: Exercise

   Record your own sound effect with the Audacity software and play it in your program.


Displaying text
---------------

Simple game where you press the space bar as fast as you can. It
displays score on screen.

Note that text is 2d, not 3d, so it must be drawn in ``draw2d()``
function not the normal ``draw()`` function.

.. literalinclude:: programs/rl_displaying_text.py
   :caption: Sound effects
   :name: code-rl_displaying_text
   :linenos:



.. topic:: Exercise

   Make the score text larger and `RED` coloured.


.. topic:: Advanced

   Create a `score2` variable for player 2 that increases when P key is pressed and display it.


.. topic:: Exercise

   Add a score to one of your other programs and display it.

