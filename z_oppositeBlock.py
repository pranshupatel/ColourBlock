"""Author: Long Uy Nguyen"""

from block import Block
from node import Node
from grid import Grid
from typing import List


class Z_oppositeBlock(Block):
    """
    Represent a Z-opposite block with the following (*) node locations
      * *
    * *
    default colour is (255, 255, 0)
    Take in the list of nodes in grid as parameter to render this block
    """
    _nodes = List[Node]  # List of nodes of this Z_oppositeBlock
    _snapshots: int

    def __init__(self, g: Grid):
        colour = (255, 255, 0)
        super().__init__("Z-opposite Block", colour, g.get_nodes())
        self._default_colour = g.get_colour()
        self.initialize_nodes()

    def initialize_nodes(self):
        """
        Create the Z-oppositeBlock object with nodes
        """
        node1 = self.grid[1][4]
        node2 = self.grid[1][3]
        node3 = self.grid[0][4]
        node4 = self.grid[0][5]
        self._nodes = [node1, node2, node3, node4]
        for node in self._nodes:
            node.set_colour(self.colour)
        self._snapshots = 1

    def move_left(self):
        """
        Move this TBlock to the left
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
        Move the node of this TBlock to the right
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
        Move this TBlock to the right
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
        Move the TBlock's node down 1 row
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
        Move the TBlock down 1 row
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
        requires implementation
        Rotate the block 90 degree clockwise
        """
        curr_node3 = self._nodes[3].get_coords()
        curr_node1 = self._nodes[1].get_coords()
        curr_node2 = self._nodes[2].get_coords()
        if self._snapshots == 1:
            try:
                if self.grid[curr_node3[0] + 1][curr_node3[1] - 1].get_colour() \
                        == self._default_colour:
                    self._nodes[1] = self.grid[curr_node2[0]][curr_node2[1]]
                    self._nodes[2] = self.grid[curr_node3[0]][curr_node3[1]]
                    self._nodes[3] = self.grid[curr_node3[0] + 1][
                        curr_node3[1] - 1]
                    self._nodes[3].set_colour(self.colour)
                    self.grid[curr_node1[0]][curr_node1[1]].reset_colour()
                    self._nodes[3].set_control(True)
                    self.grid[curr_node1[0]][curr_node1[1]].set_control(False)
                    self._snapshots = 2
            except IndexError:
                pass
        elif self._snapshots == 2:
            try:
                if self.grid[curr_node3[0] - 1][curr_node3[1] - 1].get_colour() \
                        == self._default_colour:
                    self._nodes[1] = self.grid[curr_node2[0]][curr_node2[1]]
                    self._nodes[2] = self.grid[curr_node3[0]][curr_node3[1]]
                    self._nodes[3] = self.grid[curr_node3[0] - 1][
                        curr_node3[1] - 1]
                    self._nodes[3].set_colour(self.colour)
                    self.grid[curr_node1[0]][curr_node1[1]].reset_colour()
                    self._nodes[3].set_control(True)
                    self.grid[curr_node1[0]][curr_node1[1]].set_control(False)
                    self._snapshots = 3
            except IndexError:
                pass
        elif self._snapshots == 3:
            try:
                if self.grid[curr_node3[0] - 1][curr_node3[1] + 1].get_colour() \
                        == self._default_colour:
                    self._nodes[1] = self.grid[curr_node2[0]][curr_node2[1]]
                    self._nodes[2] = self.grid[curr_node3[0]][curr_node3[1]]
                    self._nodes[3] = self.grid[curr_node3[0] - 1][
                        curr_node3[1] + 1]
                    self._nodes[3].set_colour(self.colour)
                    self.grid[curr_node1[0]][curr_node1[1]].reset_colour()
                    self._nodes[3].set_control(True)
                    self.grid[curr_node1[0]][curr_node1[1]].set_control(False)
                    self._snapshots = 4
            except IndexError:
                pass
        elif self._snapshots == 4:
            try:
                if self.grid[curr_node3[0] + 1][curr_node3[1] + 1].get_colour() \
                        == self._default_colour:
                    self._nodes[1] = self.grid[curr_node2[0]][curr_node2[1]]
                    self._nodes[2] = self.grid[curr_node3[0]][curr_node3[1]]
                    self._nodes[3] = self.grid[curr_node3[0] + 1][
                        curr_node3[1] + 1]
                    self._nodes[3].set_colour(self.colour)
                    self.grid[curr_node1[0]][curr_node1[1]].reset_colour()
                    self._nodes[3].set_control(True)
                    self.grid[curr_node1[0]][curr_node1[1]].set_control(False)
                    self._snapshots = 1
            except IndexError:
                pass
