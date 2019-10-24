
""" Author Ajitesh Misra
"""

from typing import List, Dict, Tuple


class Node:
    """ NODE CLASS
        Represents a node on the 20 x 10 grid
        Each node is 38 x 38 PIXELS long
        === Public Variables ===
        colour - The current colour of the node, can be changed

        === Private Variables ===
        _position - Tuple of ints that represents the TOP LEFT position of the node
        _background_colour - The default colour this node should be
        _length - the side length of each node in PIXELS
    """
    colour: Tuple[int, int, int]

    _position: Tuple[int, int]
    _background_colour: str
    _length: int

    def __init__(self, colour: Tuple[int, int, int], pos: Tuple[int, int], side_length: int):
        """ Initialize a new node at a given position and colour.
            Background is also set here

            pos is the TOP LEFT of the node
        """
        self.colour = colour
        self._background_colour = colour
        self._position = pos
        self._length = side_length

    def get_position(self) -> Tuple[int, int]:
        """ Return the position of the node
        """
        return self._position

    def get_colour(self) -> Tuple:
        """ Return the colour of the node
        """
        return self.colour

    def get_length(self) -> int:
        """ Return the length of the node
        """
        return self._length

    def set_colour(self, new_colour: str) -> None:
        """ Set the colour of this node to <new_colour>
        """
        self.colour = new_colour

    def reset_colour(self) -> None:
        """ Reset the node to the background colour
        """
        self.colour = self._background_colour

    def __str__(self):
        """ String representation of a node object
            -> node at [self.position]
        """
        #return "{}{}".format("node at ", self._position)
        return str(self._position)

    def __repr__(self):
        """ how python will represent a node object
            -> node at [self.position]
        """
        return self.__str__()
