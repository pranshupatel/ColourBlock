from typing import Dict, List, Tuple


class Block:
    """
    Representing a block in the game ColourBlock
    This is an abstract class, meant to be extended further depending on the
    type of block inheriting this class
    _left, _right, _top, _bottom are boolean representing the location of the
    nodes, forming a 'block'
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

    def initialize_nodes(self):
        pass

    def is_in_control(self):
        return self._in_control

    def move_left(self):
        pass

    def move_right(self):
        pass

    def rotate(self):
        pass
