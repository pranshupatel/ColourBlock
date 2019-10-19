from block import Block
from node import Node


class SquareBlock(Block):
    """
    Represent a 2x2 square block with following (*) nodes location
    * *
    * *
    default colour is (0, 255, 255)
    """
    _nodes = list(Node)
    def __init__(self):
        colour = (0, 255, 255)
        super().__init__("Square", colour)
        self.initialize_nodes()

    def initialize_nodes(self):
        """
        Create the block object with nodes
        """
        node1 = Node(self.colour, (152, 114), 38)
        node2 = Node(self.colour, (190, 114), 38)
        node3 = Node(self.colour, (152, 152), 38)
        node4 = Node(self.colour, (190, 152), 38)
        self._nodes = [node1, node2, node3, node4]

    def move_left(self):
        """
        Move this SquareBlock to the left
        """
        for node in self._nodes:
            node.move(-38, 0)

    def move_right(self):
        """
        Move this SquareBlock to the right
        """
        for node in self._nodes:
            node.move(38)

    def rotate(self):
        """
        requires implementation
        Rotate the block 90 degree clockwise
        """
        pass
