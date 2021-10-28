Arcade games
============

Collisions
----------

Arcade games need to know when one Actor sprite has hit another Actor
sprite. Most of this code is copied from
:numref:`code-moving_boxes` and
:numref:`code-keyboard_input`.

.. literalinclude:: programs/15_collisions.py
   :caption: Collisions
   :name: code-collisions
   :linenos:



.. topic:: Exercise

   Add vertical movement (as you did in Exercise \ref{exercise:updown}).


.. topic:: Advanced

   Make the box chase the alien.


.. topic:: Advanced

    Print number of times the box hits the alien (i.e. the score).




Chase
-----

Instead of moving constantly to the right we can make the movement
conditional with an ``if`` statement so the box chases the alien. Most
of this code is copied from :numref:`code-collisions`.
New lines are highlighted. We have also changed what happens when the
box catches the alien: the program now exits and you must run it again
to play again. This may not be what you want in your game!

.. literalinclude:: programs/15b_chase.py
   :emphasize-lines: 18-23
   :caption: Alien chase
   :name: code-chase
   :linenos:



.. topic:: Exercise

   Add vertical movement (as you did in previous exercise).


.. topic:: Advanced

   Draw a new enemy image.  Save it as `enemy.png` in your `mu_code/images` folder. Load it as an `Actor('enemy')` instead of the `Rect()`.




Powerup
-------

Instead of an enemy the box here is a powerup that the player must
collect. When he does it disappears and moves to a new location.

.. literalinclude:: programs/15c_powerup.py
   :caption: Collect the powerups
   :name: code-powerup
   :linenos:



.. topic:: Exercise

   Add vertical movement (as you did in Exercise \ref{exercise:updown}).




.. topic:: Exercise

   Draw a new powerup image.  Save it as `powerup.png` in your `mu_code/images` folder. Load it as an `Actor('powerup')` instead of the `Rect()`.


.. topic:: Advanced

   Combine this program with the enemy from  Program :numref:`code-chase` and the background from :numref:`code-background` and whatever else you want to make your own game.




Sound and animation
-------------------

Pygame Zero comes with one other image ``alien_hurt.png`` and one sound
``eep.wav``. If you want more you will have to add them to the
``sounds`` and ``images`` folders.

Most of this code is copied from
:numref:`code-collisions`

.. literalinclude:: programs/16_collisions2_sound_animation.py
   :emphasize-lines: 19-24
   :caption: Sound and animation upon collision
   :name: code-collisions2
   :linenos:



.. topic:: Exercise

   Record your own sound effect and add it to the game.


.. topic:: Advanced

   Add more boxes or sprites that move in different ways for the player to avoid.


.. topic:: Advanced

   Add a second alien controlled by different keys or gamepad for player 2.




Mouse clicks
------------

This uses a *function call-back* for event-based input. It is similar
to :numref:`code-collisions2` but:

-  The box has been removed.
-  There is an ``on_mouse_down()`` special function that is called
   automatically when the player click the mouse.
-  The score is displayed.

See :numref:`code-functions` for more about functions.

.. literalinclude:: programs/17_mouse_input.py
   :caption: Getting input from mouse clicks
   :name: code-mouse_input
   :linenos:





Mouse movement
--------------

.. literalinclude:: programs/18_mouse_movement.py
   :caption: Getting input from mouse movement
   :name: code-mouse_movement
   :linenos:



.. topic:: Exercise

   What happens if you delete line 8 and replace it with this::

        animate(alien, pos=pos, duration=1, tween='bounce_end')



.. topic:: Exercise

   What happens if you change `on_mouse_move` to `on_mouse_down`?


.. topic:: Advanced

   Make a game with one alien controlled by mouse and another controlled by keyboard

