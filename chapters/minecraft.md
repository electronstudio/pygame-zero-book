# Minecraft

The Minecraft Python library is made by David Whale and Martin O'Hanlon.  I highly recommend their book *Adventures in Minecraft* which contains a great deal more programs.

## Setup

You will need to own Minecraft **Java Edition**.  [https://my.minecraft.net/en-us/store/minecraft/)](https://my.minecraft.net/en-us/store/minecraft/)

If you already have a Mojang account, click login.  If you haven't accessed it for years you may need to reset your password.  If you already own Minecraft it will then tell you.  If you don't have a Mojang account, create one, and buy Minecraft Java Edition.

### Setup Java

You need to install Java Runtime Environment version 8.

Download for Windows: [https://github.com/frekele/oracle-java/releases/download/8u212-b10/jre-8u212-windows-x64.exe](https://github.com/frekele/oracle-java/releases/download/8u212-b10/jre-8u212-windows-x64.exe)

Download for Mac: [https://github.com/frekele/oracle-java/releases/download/8u212-b10/jre-8u212-macosx-x64.dmg](https://github.com/frekele/oracle-java/releases/download/8u212-b10/jre-8u212-macosx-x64.dmg)

### Setup Server

Download the Adventures In Minecraft Starter Kit from

[https://adventuresinminecraft.github.io/](https://adventuresinminecraft.github.io/) and unpack it in a folder on your desktop.
There are videos on the site that explain how to set it up. 

I suggest before you first run the server you edit the file *Server/server.properties* (use Notepad or [SublimeText](https://www.sublimetext.com/)) and change

    level-type=flat

to generate a flat world.  (But it's up to you what sort of world you prefer!)

To run the server, double click the *StartServer* file.  It will open a server console window, and ask you press space. 

If you want to generate another world later you can change

    level-name=world2

and then run the server again.

Once server is running, to stop nighttime from happening I suggest you type this at the server console

    gamerule doDaylightCycle false
    time set day

If only we could do that in real life!

You must leave the server console window open at all times.  When you want to quit, first type

    stop

at the server console, so it saves your world.

### Setup Minecraft

Run the Minecraft launcher you downloaded from minecraft.net.  We will not be using the default which is the latest version of Minecraft.  Instead we will be using **version 1.12**.

Click *launch options* then *add new*, then set version to *release 1.12*.  Then click *save*.  Then click *Minecraft* at the top.  Then click the arrow next to *Play* at the bottom.  Then select *1.12*.  Then click *Play*.

Minecraft will run.  Click 'multiplayer'.  Then 'add server'.  Enter the server address as

    localhost

Click 'done'.  Click on your server to connect to it.

### Setup Mu

Mu is the Python editor we have already been using, so you probably already have it installed.  However you need to make sure you have the latest *alpha version 1.1*, not the regular 1.0.
You can download it from the links at the *top* of [https://codewith.mu/en/download](https://codewith.mu/en/download).

Run Mu.  Click *Mode* and select *Python3*.

Then click the small gadget icon in the bottom right hand corner of the window.  Click 'third party packages'.  Type

    mcpi

Into the box.  Click OK.  The library will download.

If you are using a different editor you can install mcpi from the command line:

    pip3 install mcpi
    
## Hello Minecraft

This program tests you have a connection to the Minecraft server and displays a message on the client.

\begin{codelisting}
\codecaption{Hello, Minecraft}
\label{code:hellominecraft}
<<(programs/e00_hello.py)
\end{codelisting}

## Coordinates

This program gets the player's co-ordinates and prints them to the chat.

\begin{codelisting}
\codecaption{Getting player coordinates}
\label{code:minecoordinates}
<<(programs/e01_coordinates.py)
\end{codelisting}

\newpage

## Changing the player's position

Find the coordinates of a location in your world, either by pressing F3 in the game, or running Program~\ref{code:minecoordinates}
Enter these coordinates in this program and run it to teleport to that location.

\begin{codelisting}
\codecaption{Changing the player's position}
\label{code:telport}
<<(programs/e02_teleport.py)
\end{codelisting}

## Build a teleporter

Before you run this program, build two tiles in the game to be your teleporters and write down their co-ordinates.

\begin{codelisting}
\codecaption{Teleporter}
\label{code:telport2}
<<(programs/e03_teleport2.py)
\end{codelisting}

* Add this line to the end of the program:
```python
time.sleep(5)
```

Then add another line that teleports the player somewhere else.

## Teleport player into the air

\begin{codelisting}
\codecaption{Teleport player into the air}
\label{code:telport3}
<<(programs/e04_teleport3.py)
\end{codelisting}

## Teleport jump

This program does a series of teleports in quick succession to give the effect of a jump.

\begin{codelisting}
\codecaption{Teleport jump}
\label{code:telport4}
<<(programs/e05_teleport4.py)
\end{codelisting}


*  Change the height of the jump.
*  Make the jump faster.
*  Move the player in X and Z directions as well as Y during the jump.
*  Instead of checking if player is on a single teleporter tile, check if player is within a larger area.  Use `<`, `and`, `>` operators.

## Create a block

This program creates a block.  Each type of block has it's own number, but if we import `mcpi.block` we can use names instead remembering numbers .


\begin{codelisting}
\codecaption{Create a block}
\label{code:create_block}
<<(programs/e06_create_block.py)
\end{codelisting}

* Make the block appear a short distance from the player

\newpage

## Types of block

| AIR | BED | BEDROCK |
| BEDROCK_INVISIBLE | BOOKSHELF | BRICK_BLOCK |
| CACTUS | CHEST | CLAY |
| COAL_ORE | COBBLESTONE | COBWEB |
| CRAFTING_TABLE | DIAMOND_BLOCK | DIAMOND_ORE |
| DIRT | DOOR_IRON | DOOR_WOOD |
| FARMLAND | FENCE | FENCE_GATE |
| FIRE | FLOWER_CYAN | FLOWER_YELLOW |
| FURNACE_ACTIVE | FURNACE_INACTIVE | GLASS |
| GLASS_PANE | GLOWSTONE_BLOCK | GOLD_BLOCK |
| GOLD_ORE | GRASS | GRASS_TALL |
| GRAVEL | ICE | IRON_BLOCK |
| IRON_ORE | LADDER |
| LAPIS_LAZULI_ORE | LAVA | LAVA_FLOWING |
| LAVA_STATIONARY | LEAVES | MELON |
| MOSS_STONE | MUSHROOM_BROWN | MUSHROOM_RED |
| OBSIDIAN | REDSTONE_ORE | SAND |
| SANDSTONE | SAPLING | SNOW |
| SNOW_BLOCK | STAIRS_COBBLESTONE |
| STAIRS_WOOD | STONE | STONE_BRICK |
| STONE_SLAB | STONE_SLAB_DOUBLE | SUGAR_CANE |
| TNT | TORCH | WATER |
| WATER_FLOWING | WATER_STATIONARY | WOOD |
| WOOD_PLANKS | LAPIS_LAZULI_BLOCK | WOOL |

