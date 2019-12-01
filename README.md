# Colour Block

![Colour Block Logo](/images/colourblock-final-2.png)

Created by: Ajitesh Misra, Pranshu Patel, Harvin Lachhar, Long Uy (Wilson) Nguyen, Yan Chen (Ryan) Huang

# Table of Contents

<a name="top"></a>
1. Project Description
2. How to Install and Run Colour Block
3. How to Play Colour Block
4. High-level Code Documentation
5. Description of Directory Structure
6. Major Classes
7. Major Methods
8. How to Extend Colour Block
9. Closing

< TODO - before December 4: place the license notice here >

![Colour Block Tiny Logo](/images/colourblock-tiny.png)

## Project Description

Colour Block is a recreation of classic Tetris. From the top of the screen, blocks made up of four squares fall to the bottom of the 20-by-10 grid. These blocks can move left and right and rotate clockwise while they fall. Once these blocks hit the bottom, though, they can no longer move. The goal is to fill up and clear each row of the grid with squares. If the player cannot clear rows fast enough, the blocks will pile up and fill the grid. Once immovable blocks go out of bounds at the top, the game is over.

## How to Install and Run Colour Block

To install the game, the user must download [**Python 3.6**](https://www.python.org/downloads/) and install [**pygame**](https://www.pygame.org/wiki/GettingStarted), then download the Colour Block repository via the git clone command or the .zip file. At the top of this repository page (https://github.com/pranshupatel/ColourBlock) is a **Clone or download** button, where the .zip file to download and the link to clone the repository are both available.

To run the game, simply run game.py from the Python console, a command line, or any other program that runs Python code.

## How to Play Colour Block

![Colour Block Gameplay](/images/gameplay.png)

Use the **left and right arrow keys** to move blocks.

The **up key** rotates blocks in a clockwise manner.

The **down key** speeds up the fall.

You earn points for clearing lines.

The **escape key (Esc)** pauses the game.

## High-level Code Documentation

The game uses the MVC Design pattern. To run it, simply create an instance of the Player class. 

The Player class creates an instance of the Grid (back end) and Visual (front end) classes.

## Description of Directory Structure



## Major Classes

* Node: the squares that make up the blocks
* Grid: the back end of the game that contains all the nodes and blocks
* Block: the blocks which the user controls as they fall to the bottom
* Visuals: the front end of the game that renders the graphics
* Player: the class that processes most inputs and creates new instances of other classes

## Major Methods



## How to Extend Colour Block



## Closing

[insert closing here]
