"""Author: Long Uy Nguyen"""

from typing import Dict, List, Tuple


class Block:
    """
    Representing a block in the game ColourBlock
    This is an abstract class, meant to be extended further depending on the
    type of block inheriting this class
    colour represent the colour of the respective blocks
    _blocks represents the Tuple (nodes) that the block is consisted of
    _in_control is a bool representing whether the user is in control of this
    block
    """
    _in_control = bool
    _name = str
    colour = Tuple[int, int, int]

    def __init__(self, name,  colour):
        self._name = name
        self.colour = colour
        self._in_control = True

    def initialize_nodes(self):
        """
        Initialize the nodes for the block
        """
        pass

    def is_in_control(self):
        return self._in_control

    def change_in_control(self):
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

    def rotate(self):
        pass

    def traverse_down_1row(self):
        """
        Move the block down 1 row
        """
        pass

    def move_node_left(self, node):
        """
        Move the block's node left
        :param node: Node
        """
        pass

    def move_node_right(self, node):
        """
        Move the block's node left
        :param node: Node
        """
        pass

    def move_node_down(self, node):
        """
        Move the block's node down 1 row
        :param node: Node
        """
        pass
