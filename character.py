from typing import List, Dict, Tuple
from grid import Grid
from block import Block

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
     """
    _name: str
    _time: int
    _score: int
    _history: List[int]
    _curr_block: Block

    def __init__(self, name: str, time: int):
        """Initialize the new character entering the game."""
        self._name = name
        self._time = time
        self._score = 0
        self._history = []

    def get_name(self) -> str:
        """ Return the name of this character. """
        return self._name

    def get_score(self) -> int:
        """ Return the current character's score"""
        return self._score

    def get_history(self) -> List[int]:
        """ Return the history of the character. """

        return self._history

    def update_history(self):
        """ Update the history of this character after the current game is complete."""

        # CURRENTLY ABSTRACT
        if grid.isGameOver():
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
