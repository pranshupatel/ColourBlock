# Colour Block

![Colour Block Logo](/images/colourblock-final-2.png)

Created by Ajitesh Misra, Pranshu Patel, Harvin Lachhar, Long Uy (Wilson) Nguyen, and Yan Chen (Ryan) Huang.

Colour Block was created by a group of computer science students at the University of Toronto, Mississauga. This project was completed as part of a group assignment in the CSC290 course (Communication Skills for Computer Scientists).

![Colour Block Tiny Logo](/images/colourblock-tiny.png)

# <a name="table-of-contents"></a>Table of Contents

1. [License](#license)
2. [Project Description](#project-description)
3. [How to Install and Run Colour Block](#how-to-install-and-run)
4. [How to Play Colour Block](#how-to-play)
5. [Code Structure Overview](#code-structure-overview)
6. [Description of Directory Structure](#description-of-directory-structure)
7. [Major Classes](#major-classes)
    * [Node](#major-classes-node)
    * [Grid](#major-classes-grid)
    * [Block](#major-classes-block)
    * [Visuals](#major-classes-visuals)
    * [Player](#major-classes-player)
8. [Major Methods](#major-methods)
    * [Grid](#major-methods-grid)
    * [Block (abstract)](#major-methods-block)
    * [Visuals](#major-methods-visuals)
    * [Player](#major-methods-player)
    * [Block subclasses](#major-methods-block-subclasses)
9. [How to Extend Colour Block](#how-to-extend)
    * [Rotation](#how-to-extend-rotation)
    * [Hold feature](#how-to-extend-hold)
    * [Ghost blocks](#how-to-extend-ghost-blocks)
    * [Block previews](#how-to-extend-block-previews)
    * [Convert game file to executable](#how-to-extend-executable)
10. [Closing](#closing)
11. [Individual Contributions (Addendum)](#individual-contributions-addendum)

# <a name="license"></a>License

MIT License

Copyright (c) [2019] [Ajitesh Misra, Pranshu Patel, Harvin Lachhar, Long Uy (Wilson) Nguyen, Yan Chen (Ryan) Huang]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Return to Table of Contents](#table-of-contents)

# <a name="project-description"></a>Project Description

Colour Block is a recreation of the original version of Tetris, one of the most popular and classic puzzle video games.

## <a name="project-description-gameplay"></a>Gameplay

![Colour Block Gameplay](/images/gameplay.png)

From the top of the screen, a block made up of four squares falls to the bottom of the 20-by-10 grid. The block can move left and right and rotate clockwise while it falls. The drop speed of the block can also be increased manually. Once the block hits the bottom, though, it can no longer move and another block drops from the top of the screen.

The goal is to fill up each row of the grid with squares, and clear these rows. Clearing rows is awarded with points, with more points given for clearing more rows at once. After a row is cleared, it is filled in by the above rows which move down.

## <a name="project-description-points"></a>Points System

* Clear 1 line: 100 points
* Clear 2 lines: 200 points
* Clear 3 lines: 400 points
* Clear 4 lines: 800 points

## <a name="project-description-losing"></a>Losing Condition (Game Over)

If the player cannot clear rows fast enough, the blocks will pile up and fill the grid. Once immovable blocks fill up the grid and start to go out of bounds at the top, the game is over. Therefore, this game continues on as long as the player can clear rows quickly.

## <a name="project-description-obstacles"></a>Obstacles

The blocks fall at a speed which increases as more rows are cleared. The drop speed starts at 775 ms, and that speed decreases by 50 ms for every 2,000 points scored. For example, scoring 4,000 points would put the drop speed at 675 ms. This drop speed can decrease no further than 125 ms, which is what the drop speed is set to after scoring 26,000 points.

[Return to Table of Contents](#table-of-contents)

# <a name="how-to-install-and-run"></a>How to Install and Run Colour Block

## <a name="how-to-install-and-run-install"></a>Install Colour Block

To install the game, the user must download [**Python 3.6**](https://www.python.org/downloads/) and install [**pygame**](https://www.pygame.org/wiki/GettingStarted), then download the Colour Block repository via the git clone command or the .zip file.

One way to install pygame is to run pip install pygame from command line.

At the top of this repository page (https://github.com/pranshupatel/ColourBlock) is a **Clone or download** button, where the .zip file to download and the link to clone the repository are both available.

## <a name="how-to-install-and-run-run"></a>Run Colour Block

To run the game, simply run game.py from the Python console, a command line, or any other program that runs Python code.

[Return to Table of Contents](#table-of-contents)

# <a name="how-to-play"></a>How to Play Colour Block

* Use the **left** and **right arrow keys** to move blocks.
* The **up key** rotates blocks in a clockwise manner.
* The **down key** increases how quickly the blocks fall.
* When a row is full of blocks, it will be cleared and all the rows above it will come down. This earns points for the player.
* The **escape key (Esc)** pauses the game.

[Return to Table of Contents](#table-of-contents)

# <a name="code-structure-overview"></a>Code Structure Overview

This section provides a high-level overview of the code documentation for Colour Block.

Colour Block uses the Model-View-Controller design pattern. The file game.py creates a new instance of the Player class, which in turn creates and instance of Grid and Visuals classes. These classes work together to form the core of the gameplay.

The Grid class serves as the back-end of the game. It is an array of squares that is 24 units tall and 10 units wide. The Visuals class renders Blocks and clears them from the grid based on their colour and filled statuses.

The Visuals class is the front-end of the game. It takes in the grid from the Grid class and renders it to the screen. It also handles the pause function and allows the player to restart the game if they lose.

Further details about these classes can be found in the [Major Classes](#major-methods) section.

[Return to Table of Contents](#table-of-contents)

# <a name="description-of-directory-structure"></a>Description of Directory Structure

All of the Python files exist in the root of the directory. They are all that are required for the game to function. The **images** folder holds the images used in README.md only. The remaining folders, **.ideas**, **\_\_pycache\_\_**, and **venv**, are for development purposes.

[Return to Table of Contents](#table-of-contents)

# <a name="major-classes"></a>Major Classes

* Node: The squares that make up the blocks.
* Grid: The back end of the game that contains all the nodes and blocks (the Model).
* Block: The blocks which the user controls as they fall to the bottom.
* Visuals: The front end of the game that renders the graphics (the View).
* Player: The class that processes most inputs and creates new instances of other classes (the Controller).

## <a name="major-classes-node"></a>Node

The Node class represents one square on the grid. Each instance of Node has seven attributes:

* colour
* _background_colour (its default colour)
* _position (in pixel coordinates)
* _length (how long it is in actual pixels)
* _coords (its position in the Grid class, described below)
* _in_control (whether this node belongs to an active block)
* _filled (described in Grid)

However, the two most important attributes are colour and _coords (the coordinates).

A Block class is made up of four Node instances. When a block moves, the old nodes are reset to their original colours and the new nodes change to their block's colour. This allows the user to see the blocks fall, although this is really an illusion, as all that happens is that the nodes switch colours and _filled attributes.

The structure of the Node class allows for the easy movement and rotation of blocks. The Node class is heavily used by other objects to run the game.

## <a name="major-classes-grid"></a>Grid

The Grid class contains a collection of Node instances which are arranged into a two-dimensional list of 20 visible rows and 10 columns. (There are actually 24 rows in total, of which the top 4 rows are invisible. This helps facilitate the creation of new blocks.)

The properties of each Node instance in the Grid class can change based on various factors. For example, the _filled attribute facilitates effective collision detection, as it can change based on whether a block has hit the bottom and has another block right underneath it. As another example, the colour attributes of several Node instances change constantly as a block falls to the bottom.

Methods in the Grid class handle collision detection, check for full rows to clear, and track scores. The Grid class is heavily used by other objects to run the game.

## <a name="major-classes-block"></a>Block

![All blocks](/images/all-blocks.png)

The Block class contains a reference to four Node instances, whose coordinates are connected together to form a block. The first node in the list is regarded as the center of rotation.

This class asks the Grid instance to assign colours to the Node instances. Grid renders the blocks by accessing the colour of the block, and assigning the colour to the nodes required to facilitate the block instances.

It also contains methods to move and rotate the block, which are called from the Grid instance.

There are seven subclasses of Block, with each of them corresponding to a particular block.

Name of block | Image of block
------------- | --------------
Square-block | ![Square-block](/images/square-block.png)
Z-block | ![Z-block](/images/Z-block.png)
Z_opposite-block | ![Z_opposite-block](/images/Z-opp-block.png)
T-block | ![T-block](/images/T-block.png)
I-block | ![I-block](/images/I-block.png)
L-block | ![L-block](/images/L-block.png)
L_opposite-block | ![L_opposite-block](/images/L-opp-block.png)

## <a name="major-classes-visuals"></a>Visuals

The Visuals class uses pygame to render the graphics and the grid.

First, the class takes in an instance of Grid and renders it to the user. The way this class renders the grid is that it goes through each Node in the Grid and draws them. This happens in the render_grid method.

Next, Visuals acquires keyboard input from the user and passes it to the Player class. This is done because pygame is responsible for collecting user input, but Visuals lacks the ability to modify the Grid itself, so it passes the input to Player. The frame method handles this functionality.

Finally, the Visuals class also handles the user pausing and restarting the game. This includes stopping the movement of blocks, rendering text to tell the player the game is over/paused, and resuming the game. These are done in their own methods called pause_game and end_game. 

## <a name="major-classes-player"></a>Player

The Player class is how the player interacts with the game. It creates new instances of the Grid and Visuals classes, and interacts with them to control the gameplay. For example, it will ask the Grid instance to move a block.

This class takes input from the Visuals class, and moves or rotates a block based on the input. It also keeps track of the player's score, and stores it in a text file after the game has ended.

[Return to Table of Contents](#table-of-contents)

# <a name="major-methods"></a>Major Methods

## <a name="major-methods-grid"></a>Grid

### <a name="major-methods-grid-clear-lines"></a>clear_lines

This method first checks if the grid has a full line. If it does, it shifts the whole grid down so that the full line is now replaced with the row that was above it. This method also updates the grid's score after the line is cleared.

## <a name="major-methods-block"></a>Block (abstract)

### <a name="major-methods-block-rotate"></a>rotate (abstract)

This method rotates the specified active block by 90 degrees clockwise. It does this by adjusting the nodes that are stored in its _nodes attribute to the new rotated position. It should be accessed only through the Player class and not from any other class. It is called when the player presses the **up arrow key**.

### <a name="major-methods-block-move"></a>move_left / move_right / traverse_down_1row (abstract)

These methods move the specified block to the corresponding direction. It shifts the location of each node in the _nodes attribute by 1 unit towards the corresponsing direction. They should be accessed only through the Player class and not from any other class. The move methods are called when the player presses the corresponding **left**, **right**, or **down arrow keys**.

Further details about each of these methods can be found in the Block Subclasses subsection in Major Methods.
 
## <a name="major-methods-visuals"></a>Visuals

### <a name="major-methods-visuals-render-grid"></a>render_grid

This method is responsible for drawing the actual grid onto the pygame window. It uses information from its grid parameter, and draws it accordingly.

### <a name="major-methods-visuals-frame"></a>frame

This method is where the main loop of the game is implemented. An infinite loop constantly updates the visuals after every player action is made, such as rotate, move, pause game, or end game. The loop only terminates once the grid is completely full, or the player quits the game.

### <a name="major-methods-visuals-play"></a>play

This is the method which starts up the visuals. It initializes the pygame window, and calls the frame method in order to start up the main loop.

## <a name="major-methods-player"></a>Player

### <a name="major-methods-player-create-block"></a>create_block

This method creates a random block instance, and spawns it in the game. It sets the player's _block attribute to the block instance that was created.

### <a name="major-methods-player-move-block"></a>move_block_left, move_block_right, rotate_block, block_fall

All these methods make the specified action to the player's current block. They call the corresponding move method from the Block class that is stored in the Player class's _block attribute. Each move method checks whether the move is valid first, then makes the move if it is valid.

### <a name="major-methods-player-clear-lines"></a>clear_lines

This method simply clears the grid's full line with a call to grid.clear_lines(), and updates the player's score to match the score of the grid. It also updates the drop speed based on how large the score is (as described in the Obstacles section).

## <a name="major-methods-block-subclasses"></a>Block subclasses

Each block will have its own colour as an attribute. To obtain a different colour, simply alter this attribute. Do not change the colour of the block to the grid's colour (ie. background colour), or else the functionality of the block will not work as intended since the move validity depends on the colour difference.

### <a name="major-methods-block-subclasses-move-right"></a>move_right

Move the respective block to the right by 1 node. This method assumes the move is possible before the invocation of this method.

### <a name="major-methods-block-subclasses-move-left"></a>move_left

Move the respective block to the left by 1 node. This method assumes the move is possible before the invocation of this method.

### <a name="major-methods-block-subclasses-traverse"></a>traverse_down_1row

Move the respective block down by 1 node. This method assumes the move is possible before the invocation of this method.

### <a name="major-methods-block-subclasses-rotate"></a>rotate

Each block, except for Square-block, will have four different snapshots. Each of them represents a particular orientation of the block, or in other words, what the block looks like when it is rotated. This method checks the current snapshot and rotates to the next snapshot from the current snapshot. This method does not assume the rotation is valid, and so it checks for the validity of the rotation invocation manually.

[Return to Table of Contents](#table-of-contents)

# <a name="how-to-extend"></a>How to Extend Colour Block

## <a name="how-to-extend-rotation"></a>Rotation

One aspect to extend, or perhaps improve, is the rotation methods. Currently, with its messy manual algorithm, the code suffers from a lack of readability and performance. The methods could use better implementation. The method does the switch by changing three out of the four nodes of the block to the nodes of its next snapshot. (For non-square- and non-I-blocks, one node stays constant/unchanged as the center of rotation). One possible improvement is to have better communication between the Visuals class, the Player class, and the block in control to shorten the rotation algorithm. To follow the same design pattern with the the move validation conducted by the Player class, one could move the validity check of the rotation outside of the block classes and into the Player class. 

## <a name="how-to-extend-hold"></a>Hold feature

A feature that holds blocks into a certain space with the press of a button can be very useful for players of Colour Block. The hold feature would swap the active block with a block that it currently holds, except in cases where it is empty, in which case it just takes the block and the next block is generated as usual. Implementing such a feature does not appear to be too difficult. Simply create a new variable to represent the held block, which has an initial value of None. Then, append the frame method in the Player class to handle a key stroke that holds blocks. Such an implementation would be simple, but would not account for graphical previews, which is a far more difficult adjustment.

## <a name="how-to-extend-ghost-blocks"></a>Ghost blocks

The ghost feature would allow players to see where a block would land before it actually does. The ghost block would be under the active block at all times, and be located at the bottom-most possible location. This would be very a difficult feature to implement, based on coding the movement of the ghost block to ensure that it stays at the bottom-most possible location. A constant check for suitable ghost block locations, combined with the usage of the filled attribute in the Node class, could be a good starting point.

## <a name="how-to-extend-block-previews"></a>Block previews

Block previews would allow players to see the next few blocks before they appear. An implementation of this function would require additional random number generations, as well as an overhaul of the graphical portion of the game to store the visuals of the previews.

## <a name="how-to-extend-executable"></a>Convert game file to executable

Another aspect that can really help improve Colour Block is to convert the multi-file source folder into a Windows executable file (.exe), so that users can download and play Colour Block from any Windows computer without having to install Python and pygame. This will also clean up the game, as it will hide the implementation details and make it appear more professional.

[Return to Table of Contents](#table-of-contents)

# <a name="closing"></a>Closing

Colour Block is a rendition of the classic game of Tetris. The game is a challenge that continuously requires the player to place blocks in order to clear entire lines and score points. Colour Block has very high replayability, and is an excellent exercise for the brain. We encourage everyone to download and play Colour Block, as well as spice the game up by extending it with your own features.

[Return to Table of Contents](#table-of-contents)

# <a name="individual-contributions-addendum"></a>Individual Contributions (Addendum)

* Harvin:
  * Code contributions
    * My contributions to the code include the addition of the _filled attribute to the Node class, the addition of a method in the Grid class to fill in cleared rows by pushing down all upper rows, and the documentation of a block rotation algorithm which was later implemented. Another code contribution I made was the implementation of block drop speed decreases tied to points scored.
  * README.md contributions
    * My major contribution to the README.md file is the significant expansion of the readme with the addition of lots of information and graphics. I added in 5 new sections (Description of Directory Structure, Major Classes, Major Methods, How to Extend Colour Block, Individual Contributions) and revamped 4 existing sections (Project Description, How to Install and Run Colour Block, How to Play Colour Block, High-level Code Documentation). I added in some information into these sections as well. In particular, I added a ton of information to the Project Description section, and extended the How to Extend Colour Block section.

* Ajitesh Misra:
   * Code contributions
      * I created the Node, Grid, and Visuals classes while also adding to them as development continued. I also created game.py to allow the user to be able to run and restart the game easily. Grid and Node act as the framework for the game, allowing blocks to be moveed and rotated. It also allowed development to be clean and easy since the block implemtation does not modify that of Grid or Node. For a more detailed review, I implemented all of Visuals methods, most of Node save is_filled, and most of grid save for clear_lines. 
    * README.md contributions
        * I edited and added new additions to How to Play, Code structure and Major Classes. I also added the content of Description of Directory Structure. These new additions are further expanding on how to play by making it more descriptive, adding more detail to code structure so that it is easier to understand and expanded on the classes I worked on in the Major Classes section. For Description of Directory I explained how the code was laid out and explained the other folders used in the repo. 

* Long Uy Nguyen:
  * Code contributions
    * I implemented all aspects of blocks, including the attributes and the behaviours that all the other classes would access. The rotate implementation is directly inherited from Harvin's description/suggestion, with a slight modification that is having each rotation being a snapshot of the block to reduce duplicate checks. 
  * README.md contributions
    * I contributed to README.md by adding in the description of the major methods of blocks and editing all description related to blocks. If one wants to modify the behaviour and or the attributes of the blocks, then these areas are the main point of focus, as they are the main functionalities of all the blocks. I have also added to the "How to extend" sections the weakest part of blocks (rotate methods) that could use better implementation, or perhaps to be reinplemented if one wants to extend the block classes to improve the algorithmic runtime.

* Yan Chen (Ryan)
  * Code Contributions
    * My contribution to the code consists of the creation of test files for the Node, Grid classes in the project (node_test.py and grid_test.py).
  * README.md contributions
    * I added the closing paragraph to summarize the project as a whole. I also added the license information to the readme.

* Pranshu Patel
  * Code Contributions
    * I contributed to the code by creating and updating the player class. I created the initial layout of the player class, by planning out neccessary attributes and methods, while also implementing them as the game kept further developing. 
  * README.md contributions
    * I contributed the the README.md by adding and describing all the major methods for the Grid, Player, and Visuals classes. I also added a possible way to extend the project (by making the pygame a windows file).

[Return to Table of Contents](#table-of-contents)