"""Author: Long Uy Nguyen"""

from block import Block
from node import Node
from grid import Grid
from typing import List


class SquareBlock(Block):
    """
    Represent a 2x2 square block with following (*) nodes location
    * *
    * *
    default colour is (0, 255, 255)
    Take in the list of nodes in grid as parameter to render this block
    """
    _nodes = List[Node]  # List of nodes of this SquareBlock

    def __init__(self, g: Grid):
        colour = (0, 255, 255)
        super().__init__("Square Block", colour, g.get_nodes())
        self._default_colour = g.get_colour()
        self.initialize_nodes()

    def initialize_nodes(self):
        """
        Create the SquareBlock object with nodes
        """
        node1 = self.grid[0][4]
        node2 = self.grid[0][5]
        node3 = self.grid[1][4]
        node4 = self.grid[1][5]
        self._nodes = [node1, node2, node3, node4]
        for node in self._nodes:
            node.set_colour(self.colour)

    def move_left(self):
        """
        Move this SquareBlock to the left
        """
        l_coords = []
        for node in self._nodes:
            l_coords.append(node.get_coords())

        for i in range(len(l_coords)):
            l_coords[i] = self._move_node_left(l_coords[i])

        for i in range(len(self._nodes)):
            new_node = self.grid[l_coords[i][1]][l_coords[i][0]]
            new_node.set_colour(self.colour)
            new_node.set_control(True)
            self._nodes[i] = new_node

    def _move_node_left(self, coord):
        row = coord[1]
        col = coord[0]
        try:
            self.grid[row][col].reset_colour()
            self.grid[row][col].set_control(False)
            col -= 1
        except IndexError:
            pass

        new_coord = (col, row)
        return new_coord

    def _move_node_right(self, coord):
        """
        Move the node of this SquareBlock to the right
        :param node: Node
        """
        row = coord[1]
        col = coord[0]
        try:
            self.grid[row][col].reset_colour()
            self.grid[row][col].set_control(False)
            col += 1
        except IndexError:
            pass
        new_coord = (col, row)
        return new_coord

    def move_right(self):
        """
        Move this SquareBlock to the right
        """
        l_coords = []
        for node in self._nodes:
            l_coords.append(node.get_coords())

        for i in range(len(l_coords)):
            l_coords[i] = self._move_node_right(l_coords[i])

        for i in range(len(self._nodes)):
            new_node = self.grid[l_coords[i][1]][l_coords[i][0]]
            new_node.set_colour(self.colour)
            new_node.set_control(True)
            self._nodes[i] = new_node

    def _move_node_down(self, coord):
        """
        Move the SquareBlock's node down 1 row
        :param node: Node
        """
        row = coord[1]
        col = coord[0]
        try:
            self.grid[row][col].reset_colour()
            self.grid[row][col].set_control(False)
            row += 1
        except IndexError:
            pass

        new_coord = (col, row)
        return new_coord

    def traverse_down_1row(self):
        """
        Move the SquareBlock down 1 row
        """
        l_coords = []
        for node in self._nodes:
            l_coords.append(node.get_coords())

        for i in range(len(l_coords)):
            l_coords[i] = self._move_node_down(l_coords[i])

        for i in range(len(self._nodes)):
            new_node = self.grid[l_coords[i][1]][l_coords[i][0]]
            new_node.set_colour(self.colour)
            new_node.set_control(True)
            self._nodes[i] = new_node

    def rotate(self):
        """
        Requires implementation
        Rotate the block 90 degree clockwise
        """
        pass
