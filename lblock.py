from block import Block
from node import Node


class LBlock(Block):
    """
    Represent a L block with the following (*) node locations
    *
    *
    * *
    """

    def __init__(self):
        colour = (255, 102, 102)
        super().__init__("L Block", colour)
        self.initialize_nodes()

    def initialize_nodes(self):
        """
        Create the block object with nodes
        """
        node1 = Node(self.colour, (152, 114), 38)
        node2 = Node(self.colour, (152, 190), 38)
        node3 = Node(self.colour, (190, 190), 38)
        node4 = Node(self.colour, (152, 152), 38)
        self._nodes = [node1, node2, node3, node4]

    def move_left(self):
        """
        Move this Z-opposite Block to the left
        """
        for node in self._nodes:
            node.move(-38, 0)

    def move_right(self):
        """
        Move this Z-opposite Block to the right
        """
        for node in self._nodes:
            node.move(38)

    def rotate(self):
        """
        requires implementation
        Rotate the block 90 degree clockwise
        """
        pass

