""" This class is meant to have a grid of nodes for the game to take place on

    Author: Ajitesh Misra
"""
from typing import List, Dict, Tuple
from node import Node

class Grid:
    """ GRID CLASS
        This class is a 20 x 10 list of nodes, to be displayed to the screen

        === Private Variables === 
        _Width - the size of the game window width in PIXELS
        _Height - the size of the game window width in PIXELS 
        _NODES - The list of nodes
        _padding - the amount of PIXELS between each node
        _colour - the default colour of all nodes in the grid
        _left_offset - the distance in PIXELS from the left edge of the game window
    """

    _width: int
    _height: int
    _nodes: List[List] #of Nodes
    _padding: int
    _colour: Tuple[int, int, int]
    _left_offset: int

    def __init__(self, width: int, height: int, padding, colour: Tuple[int, int, int], offset=0):
        """ Create a new grid based on the resolution of the game window
            This is to make sure the nodes fill the height of the window while also being square

            ASSUMES: height is smaller than width

            ALL GRIDS WILL BE 20 X 10
        """
        self._width = width
        self._height = height
        self._nodes = []
        self._padding = padding
        self.colour = colour
        # if(offset):
        #     self._left_offset = offset
        # else:
        #     self._left_offset = 0

        self._left_offset = offset
        self.create_grid()

    def create_grid(self):
        """ Fill self._nodes with the array
            Creates the nodes so that they are 
        """
        # the size of each node is 1/20 the height of the grid
        real_length = self._height // 20

        # decrease the size of the node depending on the padding
        length = real_length - self._padding
        if length < 1:
            length = 1

        pos_x = self._left_offset - real_length
        pos_y = -real_length
        for x in range(20):
            self._nodes.append([])
            pos_y += real_length
            for y in range(10):
                # create a node

                # move into current positon
                pos_x += real_length

                pos = (pos_x, pos_y)
                node = Node(self.colour, pos, length)
                self._nodes[x].append(node)
            pos_x = self._left_offset - real_length

    def print_grid(self):
        """ Print the grid in a readable way
        """
        for i in self._nodes:
            print(i)

    def get_nodes(self):
        """ Return the nodes of the grids
        """
        return self._nodes

if __name__ == "__main__":
    # debug the class
    red = (255, 0, 0)
    width = 1024
    height = 768
    padding = 0
    g = Grid(width, height, padding, red)
    g.print_grid()