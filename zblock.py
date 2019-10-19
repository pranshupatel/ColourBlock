from block import Block
from node import Node


class ZBlock (Block):
    """
    Represent a Z block in ColourBlock with the following (*) node locations
    * *
      * *

    """
    _nodes = list

    def __init__(self):
        colour = (0, 255, 0)
        super().__init__("Z-block", colour)
        self. initialize_nodes()

    def initialize_nodes(self):
        """
        Create the block object with nodes
        """
        node1 = Node(self.colour, (152, 114), 38)
        node2 = Node(self.colour, (190, 114), 38)
        node3 = Node(self.colour, (190, 152), 38)
        node4 = Node(self.colour, (228, 152), 38)
        self._nodes = [node1, node2, node3, node4]

    def move_left(self):
        """
        Move this Z-Block to the left
        """
        for node in self._nodes:
            node.move(-38)

    def move_right(self):
        """
        Move this Z-Block to the right
        """
        for node in self._nodes:
            node.move(38)

    def rotate(self):
        """
        Need further implementation
        Rotate the block 90 degree clockwise

        """
