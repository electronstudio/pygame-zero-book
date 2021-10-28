Text-based quiz games
=====================

These programs can be entered using any text editor, but I suggest using
`the Mu editor <https://codewith.mu/>`__ because it comes with Python,
Pygame Zero and other libraries all pre-installed in one easy download.

Hello, world
------------

The traditional first program used to make sure Python is working and
that we can run programs.

If using the Mu editor:

1. Click the mode button and make sure the mode is set to ``Python3``.
2. Type in the program.
3. Click ``Save`` and enter a name for the program.
4. Click ``Run``.



.. code-block:: python
   :caption: Hello, world
   :name: code-hello
   :linenos:

   print("Hello world")

   # This line is a comment, you dont have to type these!


Getting input from the keyboard
-------------------------------

This program will pause and wait for you to enter some text with the
keyboard, followed by the return key. The text you enter is stored in a
variable, ``x``.

.. literalinclude:: programs/02_input.py
   :caption: Getting input from the keyboard
   :name: code-input
   :linenos:



.. topic:: Exercise

   Add some names of your friends and display a different message for each friend.


Making decisions: if, elif, else
--------------------------------

This is how to add another name to :numref:`code-input`

.. literalinclude:: programs/03_input2.py
   :emphasize-lines: 6, 7, 8, 9
   :caption: Decisions: if, elif, else
   :name: code-input2
   :linenos:



:numref:`code-input2` is very
similar to :numref:`code-input`. The new lines have
been highlighted. You can either modify
:numref:`code-input`, or else create a new file and use
copy and paste to copy the code from the old program into the new.

A random maths question
-----------------------

.. literalinclude:: programs/04_maths_question.py
   :caption: A random maths question
   :name: codemaths
   :linenos:


.. topic:: Exercise

   Add some more questions, e.g.

   * Instead of 7, use another random number.
   * Use a bigger random number.
   * Multiply (use `*`), divide (use `/`) or subtract (use `-`) numbers.



.. topic:: Exercise

   Print how many questions the player got correct at the end.




Keeping score
-------------

We create a ``score`` variable to record how many questions the player
answered correctly.


.. literalinclude:: programs/05_maths_question2.py
   :caption: Keeping score
   :name: code-maths2
   :linenos:


Guessing game with a loop
-------------------------

This ``while`` loop goes round and round forever … or until the player
gets a correct answer, and then it ``break``s out of the loop. Note
that everything in the loop is indented.


.. literalinclude:: programs/06_loop.py
   :caption: Guessing game with a loop
   :name: codeloop
   :linenos:

.. topic:: Exercise

   Give a hint to the player when they are wrong.  Was their guess too high or too low?


.. topic:: Exercise

   Print how many guesses they took to get it right at the end.




Improved guessing game
----------------------

:numref:`codeloop` with a hint whether the guess is
greater or lesser than the answer.

.. literalinclude:: programs/07_loop2.py
   :caption: GImproved guessing game
   :name: code-loop2
   :linenos:

