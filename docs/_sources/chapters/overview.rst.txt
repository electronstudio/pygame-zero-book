Overview of Python
==================

Comments
--------

A computer program is intended to be understood by both humans and
computers. However to make it easier for the humans, it can also contain
comments written in English.

.. code:: python

   # A comment looks like this

Python ignores comments. They provide explanations for the human
readers.

Literals
--------

A Python program can contain any number and any *string* of text
surrounded by quotes.

Examples:

= ==== ======= =======
5 1.23 “Hello” ‘Barry’
= ==== ======= =======

Keywords
--------

Every computer language has a number of *keywords* that you will need to
learn along with their meanings. Fortunately they look like English
words and there are only a few of them in Python. You could tick them
off as you meet them.

======= ======== ======== ====== ==== ====== ====== ======
False   None     True     and    as   assert async  await
break   class    continue def    del  elif   else   except
finally for      from     global if   import in     is
lambda  nonlocal not      or     pass raise  return try
while   with     yield                              
======= ======== ======== ====== ==== ====== ====== ======

Built-ins
---------

Python also comes with a large number of *functions*. The most common
ones are built-in and always available, much like the keywords. Here is
a list of them, just for the sake of completeness, *but you probably
won’t ever use them all*, and when you do use one you will probably look
it up in the documentation. So you *don’t need to remember these*.

========== ========== ========== ========= ========== ============
abs        all        any        ascii     bin        bool
breakpoint bytearray  bytes      callable  chr        classmethod
compile    complex    copyright  credits   delattr    dict
dir        divmod     enumerate  eval      exec       exit
filter     float      format     frozenset getattr    globals
hasattr    hash       help       hex       id         input
int        isinstance issubclass iter      len        license
list       locals     map        max       memoryview min
next       object     oct        open      ord        pow
print      property   quit       range     repr       reversed
round      set        setattr    slice     sorted     staticmethod
str        sum        super      tuple     type       vars
zip                                                   
========== ========== ========== ========= ========== ============

Once you understand all of these you effectively understand all of the
Python language. By the end of this book you will be familiar with at
least 20 keywords / functions which is enough to create a huge variety
of programs.

Libraries
---------

There are many more functions available (too many to list here), but not
everyone will need them, so they are kept in libraries. Some libraries
are supplied with Python. You can use their functions only after first
*importing* the relevant library module. For example, if you want a
random number, import the random library:

.. code:: python

   from random import randint
   print(randint(0,10))

Other libraries are not supplied with Python and must be downloaded
separately, such as the Minecraft, Pygame and Richlib libraries.

Names
-----

You will see many words in a program that appear to be English words and
yet they are not literals, keywords or library functions. These are
names chosen by the programmer. For example, if the program needs to
record a score and store it in a variable, the programmer might choose
to give that variable the name ``score``:

.. code:: python

   score = 1
   print("Score: ", score)

Python has no understanding of what ``score`` means. It only cares that
the same word is used every time. So a different programmer might decide
to write the program like this:

.. code:: python

   points = 1
   print("Score: ", points)

A programmer who doesn’t like typing might use a shorter, less
descriptive name:

.. code:: python

   p = 1
   print("Score: ", p)

However the programmer must be consistent. This **would not work**:

.. code:: python

   points = 1
   print("Score: ", score)

Whitespace
----------

Python is unusual in that it cares about *whitespace*, i.e. what you get
when you press the *tab* key or the *space* bar on the keyboard.

Python programs are arranged in blocks of lines. Every line in a block
must have the same amount of whitespace preceding it - the
*indentation*. See :numref:`code-blocks` for an
example.
