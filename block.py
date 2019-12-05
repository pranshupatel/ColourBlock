"""Author: Long Uy Nguyen"""

from node import Node
from typing import List, Tuple


class Block:
    """
    This represents a block in the game Colour Block.
    This is an abstract class, which is meant to be extended further
    depending on the type of block inheriting this class.
    The attribute colour represents the colour of the respective blocks.
    The attribute _blocks represents the Tuple of nodes that the block
    consists of.
    The attribute _in_control is a bool that represents whether the user
    is in control of the block.
    The center of rotation will always be the first node in _nodes. The
    only exception to this is the I-block.
    """
    _in_control = bool
    _name = str
    colour = Tuple[int, int, int]
    grid = List[List[Node]]

    def __init__(self, name: str,  colour: Tuple[int, int, int],
                 g: List[List[Node]]):

        self._name = name
        self.colour = colour
        self.grid = g
        self._in_control = True

    def initialize_nodes(self):
        """
        Initialize the nodes for the block
        """
        pass

    def is_in_control(self):

        """
        Return whether the block is still being controlled by the player
        :return: boolean
        """
        return self._in_control

    def change_in_control(self):
        """
        Change the in_control status to False -> the block is not being
        controlled by the player
        """
        self._in_control = False

    def move_left(self):
        """
        Move the block left
        """
        pass

    def move_right(self):
        """
        Move the block right
        """
        pass

    def traverse_down_1row(self):
        """
        Move the block down 1 row
        """
        pass

    def _move_node_left(self, node):
        """
        Move the block's node left
        :param node: Node
        """
        pass

    def _move_node_right(self, node):
        """
        Move the block's node left
        :param node: Node
        """
        pass

    def _move_node_down(self, node):
        """
        Move the block's node down 1 row
        :param node: Node
        """
        pass

    def rotate(self):
        pass
