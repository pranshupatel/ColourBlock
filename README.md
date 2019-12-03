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

## License

MIT License

Copyright (c) [2019] [Ajitesh Misra, Pranshu Patel, Harvin Lachhar, Long Uy (Wilson) Nguyen, Yan Chen (Ryan) Huang]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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

The Block class contains a reference to four Node instances, whose coordinates are connected together to form a block. The first node in the list is regarded as the center of rotation.

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

### Grid

#### clear_lines
This method first checks if the grid has a full line. If it does, it shifts the whole grid down so that the full line is now replaced with the row that was above it. This method also updates the grid's score after the line is cleared.

### Block (abstract) 

#### rotate (abstract)
This method rotates the specified block that the player currently has control of by 90 degrees. It does this by adjusting the nodes that are stored in it's _nodes attribute to the new rotated position. It should be accessed only through the player class and not from any other. It is called when the player presses the UP arrow key.

#### move_left / move_right / traverse_down_1row (abstract)
These methods move the specified block to the corresponding direction. It does this by shifting the location of each node in the _nodes attribute by 1 unit towards the corresponsing direction. They should be accessed only through the player class and not from any other. The move methods are called when the player presses the corresponding LEFT, RIGHT, or DOWN arrow keys.


### Visual

#### render_grid
This method is responsible for drawing the actual tetris board onto the pygame window. It uses information from it's grid parameter, and draws it accordingly.

#### frame
This method is where the main loop of the game is implemented. An infinite loop constantly updates the visuals after every player action is made such as rotate, move, pause game, or end game. The loop only terminates once the grid is completely full, or the player quits the game.

#### play
This is the method which starts up the visuals. It initiazes the pygame window, and calls the frame method in order to start up the main loop.

### Player

#### create_block
This method creates a random block instance, and spawns it in the game. It does this by setting the player's _block attribute to the block instance that was created.

#### move_block_left, move_block_right, rotate_block, block_fall
All these methods make the specified action to the player's current block. They do this by calling the corresponding move method from the block class that is stored in the player's _block attribute. Each move method checks whether the move is valid first, then makes the move if it is.

#### clear_lines
This method simply clears the grid's full line (by calling grid.clear_lines()) and updates the player's score to match the score of the grid.

### 7 Block subclasses

Each block will have its own colour as an attribute. If one wants a different colour, they simply need to alter this attribute (Do not change the colour of the block to the grid's colour, or else the functionality of the block will not work as intended).

#### move_right
Move the block to the right by 1 node. This method assumes the move is possible before the invocation of this method.

#### move_left
Move the block to the left by 1 node. This method assumes the move is possible before the invocation of this method.

#### traverse_down_1row
Move the block down by 1 node. This method assumes the move is possible before the invocation of this method.

#### rotate
Each block, except for the square_block, will have 4 different snapshots, each representing an orientation of the block. This method checks the current snapshot and rotate to the following snapshot from the current snapshot. This method do not assume the rotate is valid, therefore it checks for the validity of the rotation invocation manually.

[Return to Table of Contents](#table-of-contents)

## <a name="how-to-extend-colour-block"></a>How to Extend Colour Block
#### rotate
One aspect to extend or perhaps improve, is the rotation methods. Currently with its messy manual algorithm, the codes suffer from lack of readability and performance. The method does the switch by changing 3 out of the 4 nodes of the block(1 node is being represented as the center of rotation) to its next snapshot's nodes. One possible improvement is having better communication between Visual/Player and the block in control to shorten the rotate algorithm. To follow the same pattern with the verification of the move conducted by the player instance, perhaps one could move the validity check of the rotation outside of the block classes


[Return to Table of Contents](#table-of-contents)

## <a name="closing"></a>Closing

Colour Block is a rendition of the classic game of Tetris. The game provides a challenge by continuously requiring the player to find placement of blocks in order to clear entire lines and score points. Colour Block has very high replayability and is an excellent exercise for one’s brain. We encourage everyone to download and play the game as well as spicing the game up by extending it with your own features.

[Return to Table of Contents](#table-of-contents)


## <a name="individual-contributions-addendum"></a>Individual Contributions (Addendum)

* Harvin:
  * Code contributions
    * My contributions to the code include the addition of the _filled attribute to the Node class, the addition of a method in the Grid class to fill in cleared rows by pushing down all upper rows, and the documentation of a block rotation algorithm which was later implemented.
  * README.md contributions
    * My major contribution to the README.md file is the significant expansion of the readme with the addition of lots of information and graphics. I added in 5 new sections (Description of Directory Structure, Major Classes, Major Methods, How to Extend Colour Block, Individual Contributions) and revamped 4 existing sections (Project Description, How to Install and Run Colour Block, How to Play Colour Block, High-level Code Documentation). I added in some information into these sections as well. In particular, I added a ton of information to the Project Description section.

* Wilson:
  * Code contributions
    * I implemented all coding aspects of blocks and the behaviours that all the other classes will access. Rotation implementation directly inherited from Harvin's description, with slight modification that is having each rotation being a snapshot to reduce duplicate checks. 
  * README.md contributions
    * I contributed to README.md by adding in the major methods of the blocks. If one wants to modify the behaviour and attributes of the blocks, then these methods are the main point of focus, as they are the main functionalities. I have also added the section in blocks that is the weakest (rotate methods) and could use better implementation, or perhaps reimplementation if one wants to extend the block classes and to improve the algorithmic runtime. 

[Return to Table of Contents](#table-of-contents)
