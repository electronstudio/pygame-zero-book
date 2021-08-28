Advanced topics
===============

Instructor note
---------------

This introduces object oriented
programming, but I wouldn’t attempt this with young students since it
requires abstract thinking.

Classes
-------

You’ve already been using class types provided by Pygame Zero, e.g. Rect
and Actor. But if we want to store velocity as in
:numref:`code-simple_physics` we find these classes do
not include *vx* and *vy* variables inside them by default. We have to
remember to add a *vx* and *vy* every time we create an Actor.

So let’s create our own class, called *Sprite*, that is the same as
Actor but with these variables included.

.. literalinclude:: programs/26_classes.py
   :caption: Classes
   :name: code-classes
   :linenos:





Methods
-------

Classes can contain functions (called *methods*) as well as variables.
Methods are the best place to modify the class’s variables.

.. literalinclude:: programs/27_classes2.py
   :caption: Class methods
   :name: code-classes2
   :linenos:





Joystick tester
---------------

This program demonstrates using joysticks and for loops, but is mainly
included to help you test the input from your controllers.

(I don’t suggest typing this one yourself.)

.. literalinclude:: programs/19_joystick_tester.py
   :caption: Joystick tester
   :name: code-joystick_tester
   :linenos:





Distributing your Pygame Zero games
-----------------------------------

This is often tricky to get working, but you can distribute your games
to people who don’t have Python or Mu installed. You can put them on a
USB stick, or a website for people to download, or even on itch.io for
people to buy.

1. Install the full version of python from
   `www.python.org <https://www.python.org/downloads/>`__.

2. Edit your game source code (using Mu). We will assume your source is
   in a file ``MY_GAME.py``. At the top of the file add the line:

   .. code:: python

      import pgzrun

   At the bottom of the file add the line:

   .. code:: python

      pgzrun.go()

   Save the file.


4. Open a command shell: Click start menu and type ``cmd.exe``.  You should see a prompt similar to this:

   .. code::

      C:\Users\YourName>

   This means you are in the user YourName home directory, with the ``mu_code`` sub-directory inside it.
   If you are in a different directory you will have to change it with the ``cd`` command.

5. Install Nuitka and PGZero. At the command prompt type:

   .. code::

      pip install nuitka pgzero


6. Create the executable. At the command prompt type this (all one long line):

   .. code::

      python -m nuitka --onefile --include-package-data=pgzero,pygame --include-data-dir=mu_code=. --output-dir=Documents mu_code/MY_GAME.py

   Remember to replace ``MY_GAME`` with the actual name of the Python file.  If Nuitka asks for confirmation,
   type ``Yes`` and press enter.

   This will generate a program called ``MY_GAME.exe`` in your ``Documents`` folder.

7. In Windows Explorer, double click the ``MY_GAME.exe`` icon in ``Documents`` to play your game.  To distribute your game,
   copy this file.

