More advanced games
===================

These games demonstrate some essential building blocks you will need to
make more advanced games of your own.



Lists
-----

We introduced lists in :numref:`code-arrays`. In this
game, we create an empty list ``[]`` and use a loop to fill it with
alien Actors.

We again use loops to draw all the aliens and move all the aliens in the
list. When the mouse is clicked we add a new alien to the list.

.. literalinclude:: programs/21_arrays.py
   :caption: Lists are useful in games!
   :name: code-arrays2
   :linenos:



.. topic:: Advanced

   Go back to a previous game (e.g. :numref:`code-collisions`)
   and add a list of bullets that move up the screen.  When the player presses the spacebar to shoot,
   add a new bullet to the list.


Animation
---------

Animation is another use for functions. (See
:numref:`code-functions`) We define our own function
and then ask Pygame to *call it back* every 0.2 seconds. Most of this
code is from :numref:`code-collisions`.

.. literalinclude:: programs/22_animation.py
   :caption: Animation
   :name: code-animation
   :linenos:



.. topic:: Exercise

   Make the alien animate more quickly.


.. topic:: Advanced

   Add another image to the list of images.


.. topic:: Advanced

   Draw your own animation, e.g. a man walking left which plays when the left key is pressed




Simple physics
--------------

Here we draw a ball and move it, like we did in
:numref:`code-moving_boxes`. But instead of moving it
by a fixed number of pixels, we store the number of pixels to move in
variables, ``vx`` and ``vy``. These are *velocities*, i.e. speed in a
fixed direction. ``vx`` is the speed in the horizontal direction and
``vy`` is the speed in the vertical direction. This allow us to change
the velocity. Here we reverse the velocity when the ball hits the edge
of the screen.

.. literalinclude:: programs/23_simple_physics.py
   :caption: Simple physics: velocity
   :name: code-simple_physics
   :linenos:



.. topic:: Advanced

   Make the ball move faster by increasing its velocity each time it hits the sides.




Bat and ball game
-----------------

*Pong* is the classic bat and ball game.

.. literalinclude:: programs/24_pong.py
   :caption: Pong
   :name: code-pong
   :linenos:





.. topic:: Exercise

   Make the ball move more quickly.


.. topic:: Advanced

   Add another bat at the top of the screen for player 2.


.. topic:: Advanced

   Add bricks (Rects) that disappear when the ball hits them.




Timer
-----

The ``update()`` and ``draw()`` functions are called by Pygame many
times every second. Each time ``draw()`` is called we say it draws one
*frame*. The exact number of frames per second is called the *framerate*
and it will vary from one computer to another. Therefore counting frames
is not the most reliable way of keeping time.

Fortunately Pygame can tell us exactly how much many seconds have passed
since the last frame in a parameter to our update function. We use this
*delta time* to keep a timer.

.. literalinclude:: programs/28_timer.py
   :caption: Timer
   :name: code-timer
   :linenos:



.. topic:: Exercise

   Make the timer count down, not up.


.. topic:: Advanced

   Add a timer to one of your other games.


.. topic:: Advanced

   Add a timer to :numref:`code-arrays` that deletes one of the aliens when the timer runs out, then starts the timer again.




Callbacks: another kind of timer
--------------------------------

Pygame has its own clock which we can use by asking it to *callback* one
of our functions at a certain time, or regularly over and over at an
interval.

.. literalinclude:: programs/29_timer2.py
   :caption: Timer with callback functions
   :name: code-timer2
   :linenos:



.. topic:: Exercise

    Make the aliens appear more often.


.. topic:: Advanced

   Use ``len(aliens)`` to print how many aliens there are


.. topic:: Advanced

   When there are too many aliens, stop adding them using this code::

      clock.unschedule(add_alien)


