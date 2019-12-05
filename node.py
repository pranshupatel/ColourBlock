
""" Author Ajitesh Misra
"""

from typing import List, Dict, Tuple


class Node:
    """ NODE CLASS
        Represents a node on the 20 x 10 grid.
        Each node is 38 x 38 PIXELS long.
        === Public Variables ===
        colour - The current colour of the node, can be changed

        === Private Variables ===
        _position - Tuple of ints that represents the TOP LEFT position of the node
        _background_colour - The default colour this node should be
        _length - the side length of each node in PIXELS
        _coords - The coordinates of this node in the grid
        _in_control - True iff node is part of block that is in player control
        _filled - True iff node has already hit the bottom-most possible spot
    """
    colour: Tuple[int, int, int]

    _position: Tuple[int, int]
    _background_colour: str
    _length: int
    _coords: Tuple[int, int]
    _in_control: bool
    _filled: bool

    def __init__(self, colour: Tuple[int, int, int], pos: Tuple[int, int],
                side_length: int, coords: Tuple[int, int]):
        """ Initialize a new node at a given position and colour.
            The background is also set here.

            The parameter pos is the TOP LEFT of the node.
        """
        self.colour = colour
        self._background_colour = colour
        self._position = pos
        self._length = side_length
        self._coords = coords
        self._in_control = False
        self._filled = False

    def get_position(self) -> Tuple[int, int]:
        """ Return the position of the node 
            in PIXELs.
        """
        return self._position

    def get_coords(self) -> Tuple[int, int]:
        """ Return the position of this node
            in the grid.
        """
        return self._coords

    def get_colour(self) -> Tuple:
        """ Return the colour of the node.
        """
        return self.colour

    def get_background_colour(self) -> Tuple[int, int, int]:
        return self._background_colour

    def get_length(self) -> int:
        """ Return the length of the node.
        """
        return self._length

    def get_in_control(self) -> bool:
        """ Return if this node is in control.
        """
        return self._in_control

    def get_filled(self) -> bool:
        """ Return if this node is already filled.
        """
        return self._filled

    def set_colour(self, new_colour: Tuple[int, int, int]) -> None:
        """ Set the colour of this node to <new_colour>.
        """
        self.colour = new_colour

    def reset_colour(self) -> None:
        """ Reset the node to the background colour.
        """
        self.colour = self._background_colour

    def set_control(self, status) -> None:
        """ Change the status of the node if it is in control.
        """
        self._in_control = status

    def set_filled(self, new_filled: bool) -> None:
        """ Set the filled status of this node.
        """
        self._filled = new_filled

    def __str__(self):
        """ String representation of a node object
            -> node at [self.position]
        """
        #return "{}{}".format("node at ", self._position)
        return str(self._coords)

    def __repr__(self):
        """ how python will represent a node object
            -> node at [self.position]
        """
        return self.__str__()
