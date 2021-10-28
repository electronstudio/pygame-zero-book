Tutorial: Maze game
===================

In this chapter we will build a maze game together, step by step. The
Python we will use is quite simple: mostly just conditionals and loops.
The technique of creating a tilemap is common in games and after seeing
it here you should be able to incorporate it into your own projects.

.. figure:: images/figures/mazegame.png
   :width: 70%
   :alt: Maze game

   Maze game

Tilemap
-------

A tilemap uses a small number of images (the tiles) and draws them many
times to build a much larger game level (the map). This saves you from
creating a lot of artwork and makes it very easy to change the design of
the level on a whim. Here we create a maze level.

We must create three image files for the tiles: ``empty.png``,
``wall.png`` and ``goal.png`` and save them in the ``mu_code/images``
folder (accessible with the ``images`` button in Mu).

They must each be 64×64 pixels. For the player we will use the built in
``alien`` image.

.. literalinclude:: programs/maze2.py
   :caption: Drawing a tilemap
   :name: code-maze2
   :linenos:



The filenames of the tile images are stored in a *list*, ``tiles``. The
level design is stored in a list of lists, more commonly called a *two
dimensional array*. There are 8 rows and 8 columns in the array. If you
change the size of the array you will need to change the ``WIDTH`` and
``HEIGHT`` values too. The numbers in the ``maze`` array refers to
elements in the ``tiles`` array. So ``0`` means ``empty`` and ``1``
means ``wall``, etc.

.. figure:: images/figures/maze2.png
   :alt: Tile grid

   Tile grid

To draw the maze we use a ``for`` loop within another ``for`` loop. The
outer loop iterates over the rows and the inner loop iterates over the
columns, i.e. the elements of the row.



.. topic:: Exercise

   Create your own images `empty.png`, `wall.png` and `goal.png` and run the program.


.. topic:: Exercise

   The player appears at the top left of the maze at row 1 column 1.  Change the `pos` parameter so he appears at the bottom instead.


.. topic:: Exercise

   Change the design of the maze by changing the numbers in the `maze` array.


.. topic:: Advanced

   Make the maze bigger.




Moving the player
-----------------

Add this code to the *end* of the program:

.. code:: python

   def on_key_down(key):
       row = int(player.y / TILE_SIZE)
       column = int(player.x / TILE_SIZE)
       if key == keys.UP:
           row = row - 1
       if key == keys.DOWN:
           row = row + 1
       if key == keys.LEFT:
           column = column - 1
       if key == keys.RIGHT:
           column = column + 1
       player.x = column * TILE_SIZE
       player.y = row * TILE_SIZE

This function will be called automatically by Pygame, like ``draw()``
and ``update()``. However ``on_key_down()`` is not called every frame;
it is only called when the player presses a key. The key that was
pressed is passed to the function in the ``key`` *parameter*.

.. topic:: Exercise

   Run the program and move the player.  Are there any problems with the movement?




Restricting where the player can move
-------------------------------------

Delete the last two lines of the program and replace them with this
modified version:

.. code:: python

       tile = tiles[maze[row][column]]
       if tile == 'empty':
           player.x = column * TILE_SIZE
           player.y = row * TILE_SIZE
       elif tile == 'goal':
           print("Well done")
           exit()

.. topic:: Exercise

   Run the program and check that the player now *only* moves if the tile is empty.


.. topic:: Exercise

   Check that the game ends when the player reaches the goal.




Animate the movement of the player
----------------------------------

First, the alien Actor is bit too big. Draw a new image of size 64×64
pixels and save it as ``player.png`` in the ``images`` folder. In the
program, change the line:

::

   player = Actor("alien", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))

to

.. code:: python

   player = Actor("player", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))

Next, the movement of the Actor is sudden and jerky. Luckily Pygame
includes a function to do smooth movement for us automatically. Find
these lines of the program:

::

       if tile == 'empty':
             player.x = column * TILE_SIZE
             player.y = row * TILE_SIZE

replace them with:

.. code:: python

       if tile == 'empty':
           x = column * TILE_SIZE
           y = row * TILE_SIZE
           animate(player, duration=0.1, pos=(x, y))

.. topic:: Exercise

   Verify the player image has changed and moves smoothly.


Create an enemy
---------------

We will create a simple enemy that moves up and down. Add this code near
the top just *above* the ``draw()`` function.

.. code:: python

   enemy = Actor("enemy", anchor=(0, 0), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))
   enemy.yv = -1

To make the enemy visible, add this line at the end of the ``draw()``
function, after the player is drawn:

.. code:: python

     enemy.draw()

``enemy.yv`` is the velocity in the y-axis direction (up and down). Add
these lines to end of the program (still inside the ``on_key_down()``
function) to make the enemy move and reverse velocity when it hits a
wall.

.. code:: python

       # enemy movement
       row = int(enemy.y / TILE_SIZE)
       column = int(enemy.x / TILE_SIZE)
       row = row + enemy.yv
       tile = tiles[maze[row][column]]
       if not tile == 'wall':
           x = column * TILE_SIZE
           y = row * TILE_SIZE
           animate(enemy, duration=0.1, pos=(x, y))
       else:
           enemy.yv = enemy.yv * -1
       if enemy.colliderect(player):
           print("You died")
           exit()

.. topic:: Exercise

   Verify that the enemy moves up and down and kills the player.


.. topic:: Advanced

   Make another enemy that moves horizontally (left and right).


.. topic:: Advanced

   The collision detection is quite lenient (i.e. buggy) because it only tests for collisions between the
   enemy and player when a key is pressed.  Define a new function called `update()` and move the collisions detection there
   so that is called every frame.


A locked door and a key
-----------------------

We will add two new tiles to the game. Draw images ``door.png`` and
``key.png`` and save them in ``images`` folder.

Find the ``tiles`` list near the top and **change** it to include the
new images, and modify the ``maze`` with some number 3s and 4s where you
want to new tiles to appear. Mine looks like this:

.. code:: python

   tiles = ['empty', 'wall', 'goal', 'door', 'key']
   unlock = 0

   maze = [
       [1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1, 2, 0, 1],
       [1, 0, 1, 0, 1, 1, 3, 1],
       [1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 0, 1],
       [1, 0, 1, 4, 1, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1]
   ]

At the top of the program, create a new variable to store the number of
keys the player is carrying:

.. code:: python

   unlock = 0

Find the ``if`` statement where we test for ``goal``:

::

      if tile == 'goal':
           print("Well done")
           exit()

Modify it like this to also test for the key and door tiles. Since we
are modifying a *global* variable inside a function we must declare it.

.. code:: python

       global unlock
       if tile == 'goal':
           print("Well done")
           exit()
       elif tile == 'key':
           unlock = unlock + 1
           maze[row][column] = 0 # 0 is 'empty' tile
       elif tile == 'door' and unlock > 0:
           unlock = unlock - 1
           maze[row][column] = 0 # 0 is 'empty' tile



Finished game
-------------

Here is the finished game with all the changes included:

.. literalinclude:: programs/maze7.py
   :caption: Finished maze game
   :name: code-maze7
   :linenos:





Ideas for extension
-------------------

However that is not the end! There are many things you could add to this
game.

-  Show the player score.
-  Coins that the player collects to increase score.
-  Trap tiles that are difficult to see and kill the player.
-  Treasure chest that is unlocked with the key and increases score.
-  Instead of ending the game, give the player 3 lives.
-  Add more types of tile to the map: water, rock, brick, etc.
-  Change the player image depending on the direction they are moving.
