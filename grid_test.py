"""Author: Yan Chen (Ryan) Huang"""

from grid import *
import unittest
from node import *


class test_grid(unittest.TestCase):
    def setUp(self):
        """ setup the grid for testing
        """
        self.g = Grid(400, 960, 100, [1, 2, 3])
        self.g.create_grid()
        # add 3 nodes for use
        self.n1 = Node([1, 3, 5], [150, 50], 25, [1, 1])
        self.n2 = Node([1, 3, 5], [150, 50], 25, [1, 2])
        self.n3 = Node([1, 2, 3], [150, 50], 25, [1, 3])


class test_basics(test_grid):

    def test_init(self):
        """ test for initializing grid
        """
        self.assertIsNotNone(self.g, 'Failed to initialize Grid.')

    def test_gameover(self):
        """ game shouldn't be over at initialization
        """
        expected = False
        actual = self.g.is_game_over()
        self.assertEqual(expected, actual)

    def test_getscore(self):
        """ test getscore method at intialization
        """
        expected = 0
        actual = self.g.get_score()
        self.assertEqual(expected, actual)

    def test_width(self):
        """ test width initialization
        """
        expected = 400
        actual = self.g._width
        self.assertEqual(expected, actual)

    def test_height(self):
        """ test height initialization
        """
        expected = 960
        actual = self.g._height
        self.assertEqual(expected, actual)

    def test_colour(self):
        """ test colour initialization method
        """
        expected = [1, 2, 3]
        actual = self.g.get_colour()
        self.assertEqual(expected, actual)

    def test_padding(self):
        """ test padding initialization
        """
        expected = 100
        actual = self.g._padding
        self.assertEqual(expected, actual)


class test_methods(test_grid):

    def test_linefull1(self):
        """ test with all blocks filled
        """
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        self.g._nodes[24].append(self.n1)
        expected = True
        actual = self.g.is_line_full(24)
        self.assertEqual(expected, actual)

    def test_linefull2(self):
        """ test with 1 block filled
        """
        self.g._nodes[23].append(self.n1)
        expected = False
        actual = self.g.is_line_full(23)
        self.assertEqual(expected, actual)

    def test_linefull3(self):
        """ test with n3 (same colour as the background)
        """
        self.g._nodes[22].append(self.n1)
        self.g._nodes[22].append(self.n3)
        self.g._nodes[22].append(self.n2)
        expected = False
        actual = self.g.is_line_full(22)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main(exit=False)
