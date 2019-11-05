from typing import List, Dict, Tuple
from grid import Grid
from visuals import Visuals
from random import randint as rand
import pygame

# import all the blocks
import block
import iblock
import l_oppositeblock
import lblock
import squareblock
import tblock
import z_oppositeBlock
import zblock

""" ===== CONSTANTS ===== """

""" === ORIGIN ==="""
ORIGIN = (0, 0)

""" === Resolution === """
WIDTH = 400 # 1024 #
HEIGHT = 600 # 768 #

""" === FONT === """
FONT = 'Consolas'

""" === CLOCK SPEED === """
TICK_LENGTH = 500

""" BACKGROUND COLOUR """
COLOUR = (0, 32, 64)

""" PADDING """
PADDING = 5

""" Author: Pranshu Patel """
class Character:

    """ CHARACTER CLASS
        This class represents a character/player in the game. It keeps track of the score and updates the score as the game is played.
        === Private Attributes ===
        _name - The name of the character.
        _time - The amount of seconds the character has been in the game.
        _score - The current score of the character.
        _history - A list containing all the scores that the character achieved in all previoius games played.
        _block - The current block that the character is in control of.
        _grid - The grid that the current game is using
        _vis - The visuals for the game
     """
    _name: str
    _time: int
    _score: int
    _history: List[int]
    _block: block.Block
    _grid: Grid
    _vis: Visuals

    def __init__(self, name: str, time: int):
        """Initialize the new character entering the game.
           Then start the game
        """
        self._name = name
        self._time = time
        self._score = 0
        self._history = []
        self._vis = Visuals(WIDTH, HEIGHT, TICK_LENGTH, FONT, self)
        self._block = None
        self.setup_grid()
        self.start_game()

    def setup_grid(self):
        """ Create an instance of grid for this player to use """
        # to centre, take centre of screen then subtract
        # the grid's width (which is HEIGHT // 2)
        left_offset = (WIDTH - (HEIGHT // 2)) // 2
        self._grid = Grid(WIDTH, HEIGHT, PADDING, COLOUR, left_offset)

    def start_game(self):
        """ Start pygame with this game """
        print("starting game")
        self.create_block()

        self._vis.play(self._grid)


    def get_name(self) -> str:
        """ Return the name of this character. """
        return self._name

    def get_score(self) -> int:
        """ Return the current character's score"""
        return self._score

    def get_history(self) -> List[int]:
        """ Return the history of the character. """

        return self._history

    def get_grid(self) -> Grid:
        """ Return a copy of the grid """
        return self._grid

    def update_history(self):
        """ Update the history of this character after the
        current game is complete."""

        # CURRENTLY ABSTRACT
        if self.get_grid.isGameOver():
            self._history.append(self._score)

    def record_history(self, path: str) -> None:
        """ Record the character's score history in a text file to
        the designated path."""

        scores_file = open(path, "w+")
        scores_file.write(self.get_name() + "'s Score History: \n")
        for score in self._history:
            scores_file.write(str(score) + "\n")

    def update_score(self) -> None:
        """ Update the current score of the current character to
        match the score of the character's grid."""

        self._score = self._grid.get_score()

    def move_block_left(self):
        """ Move the current block to the left by 1 unit."""
        if self._can_move(dir=-1):
            self._block.move_left()

    def move_block_right(self):
        """ Move the current block to the right by 1 unit."""
        if self._can_move(dir=1):
            self._block.move_right()

    def _can_move(self, dir=0) -> bool:
        """ return true if the block can move in given direction
            -1 means left, 1 means right
            Stops the block from wrapping the grid 
            ie moving from col 0 to col 9            
        """
        if not (dir == 1 or dir == -1):
            return False

        nodes = self._block._nodes

        # move dict maps -1 to left col, 1 to right
        move_dict = {-1:0, 1:9}

        for n in nodes:
            if n.get_coords()[0] == move_dict[dir]:
                return False
        return True

    def rotate_block(self):
        """ Rotate the current block 90 degrees clockwise."""
        self.rotate()

    def create_block(self) -> None:
        """ Spawn in a random block in the
            top rows of the grid
        """
        # DO NOT MAKE A NEW BLOCK
        # TILL THE OLD ONE IS GONE
        if self._block:
            return

        block_type = rand(0, 0)
        print("block type = ", block_type)
        # begin switch case
        if block_type == 0:
            self._block = iblock.IBlock(self._grid)
        elif block_type == 1:
            self._block = l_oppositeblock.L_oppositeBlock(self._grid)
        elif block_type == 2:
            self._block = lblock.LBlock(self._grid)
        elif block_type == 3:
            self._block = squareblock.SquareBlock(self._grid)
        elif block_type == 4:
            self._block = tblock.TBlock(self._grid)
        elif block_type == 5:
            self._block = z_oppositeBlock.Z_oppositeBlock(self._grid)
        elif block_type == 6:
            self._block = zblock.ZBlock(self._grid)

        self.set_block_control(True)

    def play_move(self, move=0, speed_down=False, rotate=False) -> None:
        """ Play one move in the game

            move represents the players move direction
            -1: move block left
             1: move block right
             anything else do nothing

            rotate: if true, rotate the block
            speed down: if true blocks falls at faster rate
        """
        if not self._block:
            print("no block")
            return

        if speed_down:
            # add implementation
            pass
        if move == -1:
            self.move_block_left()
        elif move == 0:
            self._block.rotate()
        elif move == 1:
            self.move_block_right()

    def block_fall(self):
        """ Move the current block down by 1 row
            If it can, otherwise make new block

            Afterwards check if lines are full
        """

        # Check if any lines are filled
        self.clear_lines()

        # do nothing if there is no block
        if not self._block:
            return

        # NOTE: check if block can move down
        lowest_y = 0
        # store ref to grid's background colour for later
        colour = self._grid.get_colour()
        grid_nodes = self._grid.get_nodes()

        for node in self._block._nodes:
            # get pos from the node
            # NOTE: pos is in pixel coordinates
            pos = node.get_coords()
            x = pos[0]
            y = pos[1]

            # NOTE: int div to round down
            if y >= 23:
                # bottom of grid, do not go down
                # stop control of block
                self.set_block_control(False)
                self.set_block_filled(True)
                self._block = None
                self.create_block()
                return
            # Add way to check nodes below it
            # without checking the block itself

            below = grid_nodes[y+1][x]
            if (not below.get_in_control()) and \
                below.get_colour() != colour and \
                below.get_filled():
                # node below is not this block
                # and occupies
                self.set_block_control(False)
                self.set_block_filled(True)
                self._block = None
                self.create_block()
                return

        if self._block:
            self._block.traverse_down_1row()

    def clear_lines(self) -> None:
        """ check if anylines are full on the grid
            grid will clear them for us and update the score

            Then we update the score in this class
        """
        self._grid.clear_lines()
        self.update_score()

    def set_block_control(self, status) -> None:
        """ Set the status of each node of the curr
            block to <status>
        """
        if not self._block:
            return

        for i in range(len(self._block._nodes)):
            self._block._nodes[i].set_control(status)

    def set_block_filled(self, status) -> None:
        """ Set the filled status of each node of
            the curr block to <status>
        """
        if not self._block:
            return

        for i in range(len(self._block._nodes)):
            self._block._nodes[i].set_filled(status)

if __name__ == "__main__":
    player = Character("player 1", 500)
