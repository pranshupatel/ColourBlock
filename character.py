from typing import List, Dict, Tuple
from grid import Grid
from block import Block
from visuals import Visuals
import pygame

""" ===== CONSTANTS ===== """

""" === ORIGIN ==="""
ORIGIN = (0, 0)

""" === Resolution === """
WIDTH = 400 # 1024 #
HEIGHT = 600 # 768 #

""" === FONT === """
FONT = 'Consolas'

""" === CLOCK SPEED === """
TICK_LENGTH = 750

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
        _curr_block - The current block that the character is in control of.
		
		_grid - The grid that the current game is using
		_vis - The visuals for the game
     """
    _name: str
    _time: int
    _score: int
    _history: List[int]
    _curr_block: Block
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
        self._vis = Visuals(WIDTH, HEIGHT, TICK_LENGTH, FONT)
        self.setup_grid()
        self.start_game()

    def setup_grid(self):
        """ Create an instance of grid for this player to use """
        # to centre, take centre of screen then subtract the grid's width (which is HEIGHT // 2)
        left_offset = (WIDTH - (HEIGHT // 2)) // 2
        self._grid = Grid(WIDTH, HEIGHT, PADDING, COLOUR, left_offset)

    def start_game(self):
        """ Start pygame with this game """
        print("starting game")
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
        """ Update the history of this character after the current game is complete."""

        # CURRENTLY ABSTRACT
        if self.get_grid.isGameOver():
            self._history.append(self._score)
			
    def update_score(self):
        """ Update the current score accordingly once the grid detects a line is full. """
        # NEEDS TO BE IMPLEMENTED
        pass

    def move_block_left(self):
        """ Move the current block to the left by 1 unit."""
        self._block.move_left()

    def move_block_right(self):
        """ Move the current block to the right by 1 unit."""
        self._block.move_right()

    def rotate_block(self):
        """ Rotate the current block 90 degrees clockwise."""
        self.rotate()

if __name__ == "__main__":
    player = Character("player 1", 500)
