"""Author: Long Uy Nguyen"""

from block import Block
from node import Node
from grid import Grid
from typing import List


class ZBlock (Block):
    """
    Represent a Z block in ColourBlock with the following (*) node locations
    * *
      * *
    default colour is (0, 255, 0)
    Take in the list of nodes in grid to render this block
    """
    _grid = List[List[Node]]
    _nodes = List[Node]

    def __init__(self, g:Grid):
        colour = (0, 255, 0)
        super().__init__("Z-block", colour)
        self._grid_colour = g.get_colour()
        self._grid = g.get_nodes()
        self. initialize_nodes()

    def initialize_nodes(self):
        """
        Create the Zblock object with nodes
        """
        node1 = self._grid[0][4]
        node2 = self._grid[0][5]
        node3 = self._grid[1][5]
        node4 = self._grid[1][6]
        self._nodes = [node1, node2, node3, node4]

    def move_left(self):
        """
        Move this Zblock to the left
        """
        for node in self._nodes:
            self.move_node_left(node)

    def move_node_left(self, node):
        """
        Move the node of this ZBlock to the left
        :param node: Node
        """
        for l in range(len(self._grid)):
            for n in range(len(self._grid[l])):
                if self._grid[l][n] == node:
                    try:
                        index = self._nodes.index(node)
                        self._grid[l][n-1].set_colour(self.colour)
                        self._grid[l][n].set_colour(self._grid_colour)
                        self._nodes[index] = self._grid[l][n-1]
                    except IndexError:
                        continue

    def move_node_right(self, node):
        """
        Move the node of this Zblock to the right
        :param node: Node
        """
        for l in range(len(self._grid)):
            for n in range(len(self._grid[l])):
                if self._grid[l][n] == node:
                    try:
                        index = self._nodes.index(node)
                        self._grid[l][n+1].set_colour(self.colour)
                        self._grid[l][n].set_colour(self._grid_colour)
                        self._nodes[index] = self._grid[l][n+1]
                    except IndexError:
                        continue

    def move_right(self):
        """
        Move this Zblock to the right
        """
        for node in self._nodes:
            self.move_node_right(node)

    def move_node_down(self, node):
        """
        Move the Zblock's node down 1 row
        :param node: Node
        """
        for l in range(len(self._grid)):
            for n in range(len(self._grid[l])):
                if self._grid[l][n] == node:
                    try:
                        index = self._nodes.index(node)
                        self._grid[l+1][n].set_colour(self.colour)
                        self._grid[l][n].set_colour(self._grid_colour)
                        self._nodes[index] = self._grid[l+1][n]
                    except IndexError:
                        continue

    def traverse_down_1row(self):
        """
        Move the Zblock down 1 row
        """
        for node in self._nodes:
            self.move_node_down(node)

    def rotate(self):
        """
        Need further implementation
        Rotate the block 90 degree clockwise

        """
