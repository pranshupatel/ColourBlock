# Colour Block

![Colour Block Logo](/images/colourblock-final-2.png)

Created by: Ajitesh Misra, Pranshu Patel, Harvin Lachhar, Long Uy (Wilson) Nguyen, Yan Chen (Ryan) Huang

## <a name="table-of-contents"></a>Table of Contents

1. [Project Description](#project-description)
2. [How to Install and Run Colour Block](#how-to-install-and-run-colour-block)
3. [How to Play Colour Block](#how-to-play-colour-block)
4. [Code Structure (High-level Code Documentation)](#code-structure-high-level-code-documentation)
5. [Description of Directory Structure](#description-of-directory-structure)
6. [Major Classes](#major-classes)
7. [Major Methods](#major-methods)
8. [How to Extend Colour Block](#how-to-extend-colour-block)
9. [Closing](#closing)
10. [Individual Contributions (Addendum)](#individual-contributions-addendum)

< TODO - before December 4: place an extended description of authorship here >

< TODO - before December 4: place the license notice here >

![Colour Block Tiny Logo](/images/colourblock-tiny.png)

## <a name="project-description"></a>Project Description

Colour Block is a recreation of the original version of Tetris, one of the most popular and classic puzzle video games.

### Gameplay

From the top of the screen, a block made up of four squares falls to the bottom of the 20-by-10 grid. The block can move left and right and rotate clockwise while it falls. The drop speed of the block can also be increased manually. Once the block hits the bottom, though, it can no longer move and another block drops from the top of the screen.

The goal is to fill up each row of the grid with squares, and clear these rows. Clearing rows is awarded with points, with more points given for clearing more rows at once. After a row is cleared, it is filled in by the above rows which move down.

### Points System

* Clear 1 line: 100 points
* Clear 2 lines: 200 points
* Clear 3 lines: 400 points
* Clear 4 lines: 800 points

### Losing Condition (Game Over)

If the player cannot clear rows fast enough, the blocks will pile up and fill the grid. Once immovable blocks fill up the grid and start to go out of bounds at the top, the game is over. Therefore, this game lasts as long as the player can clear rows quickly.

### Obstacles

The blocks fall at a speed which increases as more rows are cleared. The drop speed starts at three-fourths of a second (750 ms), and that speed decreases by 50 ms for every 2,000 points scored. For example, scoring 4,000 points would put the drop speed at 650 ms. This drop speed can decrease no further than 125 ms, which occurs after scoring 26,000 points.

[Return to Table of Contents](#table-of-contents)

## <a name="how-to-install-and-run-colour-block"></a>How to Install and Run Colour Block

### Install

To install the game, the user must download [**Python 3.6**](https://www.python.org/downloads/) and install [**pygame**](https://www.pygame.org/wiki/GettingStarted), then download the Colour Block repository via the git clone command or the .zip file.

One way to install pygame is to run pip install pygame from command line.

At the top of this repository page (https://github.com/pranshupatel/ColourBlock) is a **Clone or download** button, where the .zip file to download and the link to clone the repository are both available.

### Run

To run the game, simply run game.py from the Python console, a command line, or any other program that runs Python code.

[Return to Table of Contents](#table-of-contents)

## <a name="how-to-play-colour-block"></a>How to Play Colour Block

![Colour Block Gameplay](/images/gameplay.png)

Use the **left and right arrow keys** to move blocks.

The **up key** rotates blocks in a clockwise manner.

The **down key** speeds up the fall.

You earn points for clearing lines.

The **escape key (Esc)** pauses the game.

[Return to Table of Contents](#table-of-contents)

## <a name="code-structure-high-level-code-documentation"></a>Code Structure (High-level Code Documentation)

The game uses the Model-View-Controller design pattern. To run it, simply create an instance of the Player class. 

The Player class creates an instance of the Grid (back-end) and Visual (front-end) classes.



[Return to Table of Contents](#table-of-contents)

## <a name="description-of-directory-structure"></a>Description of Directory Structure



[Return to Table of Contents](#table-of-contents)

## <a name="major-classes"></a>Major Classes

< TODO - before December 4: add more information to this section and organize it...it is a very disconnected collection of information right now... >

* Node: the squares that make up the blocks
* Grid: the back end of the game that contains all the nodes and blocks (the Model)
* Block: the blocks which the user controls as they fall to the bottom
* Visual: the front end of the game that renders the graphics (the View)
* Player: the class that processes most inputs and creates new instances of other classes (the Controller)

### Node

The Node class represents one square on the grid. This square is usually purple, but can be any other colour.

A Block class is made up of Node instances.

The structure of the Node class allows for easy movement and rotation of blocks. The Node class is heavily used by other objects to run the game.

### Grid

The Grid class contains a collection of Node instances arranged into a two-dimensional list of 20 visible rows and 10 columns. (There are actually 24 rows in total, of which the top 4 rows are invisible. This helps facilitate the creation of new blocks.)

The properties of each Node instance in the Grid class can change based on various factors. For example, the filled attribute that enables effective collision detection can change based on whether a block has hit the bottom and has another block right underneath it. As another example, the colour attributes of several Node instances change constantly whenever a block falls to the bottom.

Methods in the Grid class handle collision detection, check for full rows to clear, and track scores. The Grid class is heavily used by other objects to run the game.

### Block

![All blocks](/images/all-blocks.png)

The Block class contains a reference to four Node instances, whose coordinates are connected together to form a block.

This class asks the Grid instance to assign colours to the Node instances.

It also contains methods to move and rotate the block, which are called from the Grid instance.

There are seven sub-classes of Block, with each of them corresponding to a particular block.

#### Square-block

![Square-block](/images/square-block.png)

#### Z-block

![Z-block](/images/Z-block.png)

#### Z_opposite-block

![Z_opposite-block](/images/Z-opp-block.png)

#### T-block

![T-block](/images/T-block.png)

#### I-block

![I-block](/images/I-block.png)

#### L-block

![L-block](/images/L-block.png)

#### L_opposite-block

![L_opposite-block](/images/L-opp-block.png)

### Visual

The Visual class uses pygame to render the graphics and the grid.

It uses a timer to carry out its functions.

The class uses pixel coordinates.

The Visual class collects user input and sends it to the Player class. It ignores invalid commands.

Methods in the Visual class handle the pause and restart functions.

### Player

The Player class is how the player interacts with the game. It creates new instances of the Grid and Visuals classes, and interacts with them to control the gameplay. For example, it will ask the Grid instance to move a block.

This class takes input from the Visual class, and moves or rotates a block based on the input.

This class will store a block for later, which is a good feature to have because...

This class keeps track of the player's score, and stores it in a text file after the game has ended.

[Return to Table of Contents](#table-of-contents)

## <a name="major-methods"></a>Major Methods



[Return to Table of Contents](#table-of-contents)

## <a name="how-to-extend-colour-block"></a>How to Extend Colour Block



[Return to Table of Contents](#table-of-contents)

## <a name="closing"></a>Closing

[insert closing here]

[Return to Table of Contents](#table-of-contents)


## <a name="individual-contributions-addendum"></a>Individual Contributions (Addendum)

* Harvin:
  * Code contributions
    * My contributions to the code include the addition of the _filled attribute to the Node class, the addition of a method in the Grid class to fill in cleared rows by pushing down all upper rows, and the documentation of a block rotation algorithm which was later implemented.
  * README.md contributions
    * My major contribution to the README.md file is the significant expansion of the readme with the addition of lots of information and graphics. I added in 5 new sections (Description of Directory Structure, Major Classes, Major Methods, How to Extend Colour Block, Individual Contributions) and revamped 4 existing sections (Project Description, How to Install and Run Colour Block, How to Play Colour Block, High-level Code Documentation). I added in some information into these sections as well. In particular, I added a ton of information to the Project Description section.

[Return to Table of Contents](#table-of-contents)