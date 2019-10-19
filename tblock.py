from block import Block
from node import Node


class TBlock(Block):
    """
    Represent a T block with the following (*) node locations
      *
    * * *
    """

    def __init__(self):
        colour = (255, 0, 255)
        super().__init__("T Block", colour)
        self.initialize_nodes()

    def initialize_nodes(self):
        """
        Create the block object with nodes
        """
        node1 = Node(self.colour, (152, 114), 38)
        node2 = Node(self.colour, (114, 152), 38)
        node3 = Node(self.colour, (190, 152), 38)
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

