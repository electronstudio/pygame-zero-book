Python in Minecraft
===================

.. note:: The Minecraft Python library is made by David Whale and Martin O’Hanlon.
   I highly recommend their book *Adventures in Minecraft* which contains a
   great deal more programs.

Setup
-----

You will need to own Minecraft `Java Edition <https://www.minecraft.net/en-us/store/minecraft-java-edition>`_ (not Bedrock edition).

If you already have a Mojang or Microsoft account, go to the Minecraft website and click login. If you haven’t
accessed it for years you may need to reset your password. If you
already own Minecraft it will then tell you. If you don’t have an
account, create one, and buy Minecraft Java Edition.

Setup Java
~~~~~~~~~~

You will need to download and install Java from `adoptopenjdk.net <https://adoptopenjdk.net>`_.

I recommend the *latest* (currently **OpenJDK 16**) because it will be useful for other things, but if you have problems you
can fall back to using **OpenJDK 8**.  Choose **HotSpot** and click the button to download.

Setup Server
~~~~~~~~~~~~

Download the *Adventures In Minecraft Starter Kit* from

https://adventuresinminecraft.github.io and unpack it in a folder on
your desktop. There are videos on the site that explain how to set it
up.

Use Notepad or `SublimeText <https://www.sublimetext.com/>`_ to edit the file
*Server/server.properties*.  Change this setting

::

   level-type=flat

to generate a flat world. (But it’s up to you what sort of world you
prefer!)

To run the server, double click the **StartServer** file. It will open a
server console window, and ask you press space.

If you want to generate another world later you can change

::

   level-name=world2

and then run the server again.

Once the server is running, to stop nighttime from happening I suggest you
type this at the server console

::

   gamerule doDaylightCycle false
   time set day

If only we could do that in real life!

You must leave the server console window open at all times. When you
want to quit, first type

::

   stop

at the server console, so it saves your world.

.. topic:: Advanced Challenge

   Setup a more modern Minecraft server, such as `PaperMC <https://papermc.io/>`_.

   Then try to get the `Raspberryjuice plugin <https://dev.bukkit.org/projects/raspberryjuice>`_ to work with it so you can use it with Python.  This is not easy; I couldn't do it!

Setup Minecraft
~~~~~~~~~~~~~~~

Run the Minecraft launcher you downloaded from minecraft.net. We will
not be using the default which is the latest version of Minecraft.
Instead we will be using **version 1.12**.

Run the **Minecraft Launcher**.  Click **Installations** then **New Installation**, then select version **release
1.12**. Then click *Create*.  Then click **Play** next to the new installation in the list.

Minecraft will run. Click **multiplayer**. Then **add server**. Enter the
server address as

::

   localhost

Click ‘done’. Click on your server to connect to it.

Setup Mu
~~~~~~~~

Mu is the Python editor we have already been using, so you probably
already have it installed. However you need to make sure you have the
latest version. You can download it
from the links at the *top* of https://codewith.mu/en/download.

Run *Mu*. Click **Mode** and select **Python3**.  Then click *the small gadget icon* in the bottom right hand corner of the
window. Click **third party packages**. Type

::

   mcpi

into the box. Click **OK**. The library will download.

*If you are not using Mu* you can install mcpi from the
command line like this:

::

   pip3 install mcpi


Summary
~~~~~~~

.. image:: images/minecraft.png
   :width: 50%
   :align: center

You need to have the Minecraft server, Minecraft (the client) and Mu all running at the same time.  It may be
useful to arrange them in separate windows.  Your Python program will talk to the server, and Minecraft will also talk to the server,
allowing you to see the results of your program in Mincraft.

Hello Minecraft
---------------

This program tests you have a connection to the Minecraft server and
displays a message on the client.

.. literalinclude:: programs/e00_hello.py
   :caption: Hello, Minecraft
   :name: code-hellominecraft
   :linenos:



Coordinates
-----------

This program gets the player’s co-ordinates and prints them to the chat.

.. literalinclude:: programs/e01_coordinates.py
   :caption: Getting player coordinates
   :name: code-minecoordinates
   :linenos:





Changing the player’s position
------------------------------

Find the coordinates of a location in your world, either by pressing F3
in the game, or running :numref:`code-minecoordinates`
Enter these coordinates in this program and run it to teleport to that
location.

.. literalinclude:: programs/e02_teleport.py
   :caption: Changing the player's position
   :name: code-telport
   :linenos:



Build a teleporter
------------------

Before you run this program, build two tiles in the game to be your
teleporters and write down their co-ordinates.

.. literalinclude:: programs/e03_teleport2.py
   :caption: Teleporter
   :name: code-telport2
   :linenos:



.. topic:: Exercise

   Add this line to the end of the program::

        time.sleep(5)


   Then add another line that teleports the player somewhere else.



Teleport player into the air
----------------------------

.. literalinclude:: programs/e04_teleport3.py
   :caption: Teleport player into the air
   :name: code-telport3
   :linenos:



Teleport jump
-------------

This program does a series of teleports in quick succession to give the
effect of a jump.

.. literalinclude:: programs/e05_teleport4.py
   :caption: Teleport jump
   :name: code-telport4
   :linenos:



.. topic:: Exercise

   * Change the height of the jump.

.. topic:: Exercise

   * Make the jump faster.

.. topic:: Exercise

   * Move the player in X and Z directions as well as Y during the jump.


.. topic:: Advanced

   Instead of checking if player is on a single teleporter tile, check if player is within a larger area.  Use `<`, `and`, `>` operators.


Create a block
--------------

This program creates a block. Each type of block has it’s own number,
but if we import ``mcpi.block`` we can use names instead remembering
numbers.

.. literalinclude:: programs/e06_create_block.py
   :caption: Create a block
   :name: code-create_block
   :linenos:



.. topic:: Exercise

   Make the block appear a short distance from the player.




Types of block
--------------

..  list-table::
    :widths: 25 25 25

    *   - AIR
        - BED
        - BEDROCK
    *   - BEDROCK_INVISIBLE
        - BOOKSHELF
        - BRICK_BLOCK
    *   - CACTUS
        - CHEST
        - CLAY
    *   - COAL_ORE
        - COBBLESTONE
        - COBWEB
    *   - CRAFTING_TABLE
        - DIAMOND_BLOCK
        - DIAMOND_ORE
    *   - DIRT
        - DOOR_IRON
        - DOOR_WOOD
    *   - FARMLAND
        - FENCE
        - FENCE_GATE
    *   - FIRE
        - FLOWER_CYAN
        - FLOWER_YELLOW
    *   - FURNACE_ACTIVE
        - FURNACE_INACTIVE
        - GLASS
    *   - GLASS_PANE
        - GLOWSTONE_BLOCK
        - GOLD_BLOCK
    *   - GOLD_ORE
        - GRASS
        - GRASS_TALL
    *   - GRAVEL
        - ICE
        - IRON_BLOCK
    *   - IRON_ORE
        - LADDER
        -
    *   - LAPIS_LAZULI_ORE
        - LAVA
        - LAVA_FLOWING
    *   - LAVA_STATIONARY
        - LEAVES
        - MELON
    *   - MOSS_STONE
        - MUSHROOM_BROWN
        - MUSHROOM_RED
    *   - OBSIDIAN
        - REDSTONE_ORE
        - SAND
    *   - SANDSTONE
        - SAPLING
        - SNOW
    *   - SNOW_BLOCK
        - STAIRS_COBBLESTONE
        -
    *   - STAIRS_WOOD
        - STONE
        - STONE_BRICK
    *   - STONE_SLAB
        - STONE_SLAB_DOUBLE
        - SUGAR_CANE
    *   - TNT
        - TORCH
        - WATER
    *   - WATER_FLOWING
        - WATER_STATIONARY
        - WOOD
    *   - WOOD_PLANKS
        - LAPIS_LAZULI_BLOCK
        - WOOL



Create a block inside a loop
----------------------------

This program creates a block over and over again in a loop. Move around
to see it.

.. literalinclude:: programs/e07_create_block_loop.py
   :caption: Block loop
   :name: code-create_block_loop
   :linenos:



.. topic:: Exercise

   Make the block appear one meter **below** the player's position.


.. topic:: Exercise

   Change the block to something else, e.g. `ICE`


Create a tower of blocks
------------------------

We will use a ``for`` loop to easily build a tower of blocks.

.. literalinclude:: programs/e08_tower.py
   :caption: Tower of blocks
   :name: code-e08_tower
   :linenos:



.. topic:: Exercise

   How high can you make the tower?


.. topic:: Exercise

   Change the program to create *three* towers next to one another.


Clear space
-----------

The ``setBlocks()`` function lets us create a large cube of blocks. If
we create blocks of type ``AIR`` this has the effect of removing all
blocks! This is such a useful thing that we will need it in the future,
therefore in this program we put it in its own *function*. Make sure to save the
program as ``clear_space.py`` so you can ``import`` it into the next
program.

.. literalinclude:: programs/e09_clear_space.py
   :caption: Clear space
   :name: code-e09_clear_space
   :linenos:



Build a house
-------------

Make sure you have saved the previous :numref:`code-e09_clear_space` to the same directory before you run
this program because we are going to ``import`` the function from
``clear_space.py``. Save this program as ``house.py``.

.. literalinclude:: programs/e10_basic_house.py
   :caption: A simple house
   :name: code-e10_basic_house
   :linenos:



.. topic:: Exercise

   Run the program and manually bash a hole in the wall to see what is inside and to give you a way to get into the building.


.. topic:: Exercise

   Change the program so it *automatically* makes a hole for a door.


.. topic:: Exercise

   Lower the floor in your house.


.. topic:: Exercise

   Add some furniture, torches, windows.


.. topic:: Advanced

   Make the windows get bigger if you increase the size of the house.


.. topic:: Exercise

   Try filling a house with `LAVA`, or `WATER`, or `TNT` (Be careful with `TNT`, too much will crash your computer!)


Build a street of houses
------------------------

Make sure you have saved the previous :numref:`code-e10_basic_house`
to the same directory before you run
this program because we are going to ``import`` the function from
``house.py``.

.. literalinclude:: programs/e11_street.py
   :caption: A street of houses
   :name: code-e11_street
   :linenos:



.. topic:: Exercise

   How many houses are there?  Make the street longer with more houses.


.. topic:: Exercise

   Make the houses get taller as the street goes on.


.. topic:: Exercise

   Add some towers to the street.


.. topic:: Advanced

   Put a loop inside the loop to create multiple streets.


.. topic:: Advanced

   Make some roads or fences.


.. topic:: Exercise

   Make your houses out of TNT.  Use flint tool on them.


Chat commands
-------------

This program can read chat messages posted by players. It builds a block
next to any player who says “build”. This is the first example that will
work for more than one player.

.. literalinclude:: programs/e12_chat.py
   :caption: Chat commands
   :name: code-e12_chat
   :linenos:



.. topic:: Advanced

   Build a house around the player if the player says "house".


.. topic:: Advanced

   Build a lava trap if the player says "trap".


.. topic:: Advanced

   use `mc.getPlayerEntityId("fred")` to get the id of a certain player named Fred
   (or whatever your friend's player name is).  Build something at the position of this player.


Turtle
------

*This requires the* **minecraftstuff** *package to work.* You can install it
in Mu by clicking in the bottom right gadget and adding
``minecraftstuff`` to list of third party packages

In olden days at school we used robotic turtles to draw on paper.  You may have
done similar on the screen in Python or Scratch.  This is the same but
in Minecraft.

.. literalinclude:: programs/e13_turtle.py
   :caption: Turtle
   :name: code-e13_turtle
   :linenos:



.. topic:: Exercise

   Draw a triangle, hexagon, etc.


.. topic:: Exercise

   What do turtle.up(90) and turtle.down(90) do?

