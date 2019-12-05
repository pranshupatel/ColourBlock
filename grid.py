""" This class is meant to have a grid of nodes for the game to take place on.

    Author: Ajitesh Misra
"""
from typing import List, Dict, Tuple
from node import Node
from random import randint as rand

# NOTE: below doesn't work since import is circular
# from block import Block
# from iblock import IBlock
# from l_oppositeblock import L_oppositeBlock
# from lblock import LBlock
# from squareblock import SquareBlock
# from tblock import TBlock
# from z_oppositeBlock import Z_oppositeBlock
# from zblock import ZBlock
# import block
# import iblock
# import l_oppositeblock
# import lblock
# import squareblock
# import tblock
# import z_oppositeBlock
# import zblock

class Grid:
    """ GRID CLASS
        This class is a 24 x 10 list of nodes,
	though only 20 x 10 is to be displayed to the screen.
	(This is done so that new blocks are spawned off screen.)

        === Private Variables ===
        _width - the size of the game window width in PIXELS
        _Height - the size of the game window width in PIXELS
        _nodes - The list of nodes
        _padding - the amount of PIXELS between each node
        _colour - the default colour of all nodes in the grid
        _left_offset - the distance in PIXELS from the left edge of the game window
        _score - the players score so far
        _is_over - whether the game is over
    """

    _width: int
    _height: int
    _nodes: List[List[Node]] # of Nodes
    _padding: int
    _colour: Tuple[int, int, int]
    _left_offset: int
    _score: int
    _is_over: bool

    def __init__(self, width: int, height: int, padding, colour: Tuple[int, int, int], offset=0):
        """ Create a new grid based on the resolution of the game window.
            This is to make sure the nodes fill the height of the window,
	    while also being square.

            ASSUMES: height is smaller than width.

            ALL GRIDS WILL BE 24 X 10.
        """
        self._width = width
        self._height = height
        self._nodes = []
        self._padding = padding
        self._colour = colour
        self._left_offset = offset
        self._score = 0
        self._is_over = False
        self.create_grid()

    def create_grid(self) -> None:
        """ Fill self._nodes with the array.
            Creates the nodes so that they are.
        """
        # The size of each node is 1/20 the height of the grid.
        real_length = self._height // 20

        # Decrease the size of the node depending on the padding.
        length = real_length - self._padding
        if length < 1:
            length = 1

		# NOTE:
		# pos x and y need to be init 1 space before they start,
		# so that when they increment, the first node is in the
		# correct place.
        pos_x = self._left_offset - real_length
        pos_y = -real_length * 5
        for y in range(24):
            self._nodes.append([])
            pos_y += real_length
            for x in range(10):
                # Create a node

                # Move into current positon
                pos_x += real_length

                pos = (pos_x, pos_y)
                node = Node(self._colour, pos, length, (x, y))
                self._nodes[y].append(node)
			# Reset x to left
            pos_x = self._left_offset - real_length

    def print_grid(self) -> None:
        """ Print the grid in a readable way.
        """
        for i in self._nodes:
            print(i)

    def get_colour(self):
        return self._colour

    def get_nodes(self) -> List[List[Node]]:
        """ Return the nodes of the grids.
        """
        return self._nodes

    def get_score(self) -> int:
        """ Return the total score of the current game.
        """
        return self._score

    def is_line_full(self, index: int) -> bool:
        """ Return true iff line at index is full.
            i.e. : the colours of each node are different
                    than the background colour and the
		    nodes are filled.
        """
	# Go through the row and see if any nodes are not occupied.
        for node in self._nodes[index]:
            if node.get_colour() == self._colour or \
	        (not node.get_filled()):
                return False
        # All blocks are different colours and all are filled.
        return True

    def is_line_clear(self, index: int) -> bool:
        """ Return true iff line at index is clear.
            i.e. : the colours of each node are the same
                    as the background colour and the
                    nodes are not filled.
        """
	# Go through the row and see if any nodes are occupied.
        for node in self._nodes[index]:
            if node.get_colour() != self._colour or \
	        node.get_filled():
                return False
        # All blocks are the same colours and none are filled.
        return True

    def set_game_over(self) -> None:
        """ Set the game to be over.
            ONLY TO BE CALLED FROM PLAYER.
        """
        self._is_over = True

    def is_game_over(self) -> bool:
        """ Return True iff player can not make a new move.
            (The check occurs in the player script.
	    This just returns the value.)
        """
        return self._is_over

    def reset_row(self, index: int) -> None:
        """ Make the nodes of row <index> the
            background colour again and un-fill them.
        """
        for i in range(len(self._nodes[index])):
            self._nodes[index][i].reset_colour()
            self._nodes[index][i].set_filled(False)

    def clear_lines(self) -> None:
        """ Clear any lines that are full.
            Add to score as needed.
        """
        lines_cleared = 0

        # Go through the bottom rows.
        for i in range(len(self.get_nodes())):
            if self.is_line_full(i):
                # Line is full
                self.reset_row(i)
                lines_cleared += 1

        # Increase score, according to project plan.
        if lines_cleared != 0: # Only increase if line has been cleared.
            self._score += 50 * (2 ** lines_cleared)
	
	# Fill in newly cleared rows with above nodes.
        y = 23
        while y > 0:
            if self.is_line_clear(y):
                x = 0
                while x < 10:
                    self._nodes[y][x].set_colour(self._nodes[y-1][x].get_colour())
                    self._nodes[y][x].set_control(self._nodes[y-1][x].get_in_control())
                    self._nodes[y][x].set_filled(self._nodes[y-1][x].get_filled())
                    self._nodes[y-1][x].reset_colour()
                    self._nodes[y-1][x].set_control(False)
                    self._nodes[y-1][x].set_filled(False)
                    x = x + 1
            y = y - 1

