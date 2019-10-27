from grid import *
import unittest
from node import *


class test_grid(unittest.TestCase):
    def setUp(self):
        # setup the grid for testing
        self.g = Grid(400, 960, 100, [1, 2, 3])
        self.g.create_grid()
        # add 3 nodes for use
        self.n1 = Node([1, 3, 5], [150, 50], 25, [1, 1])
        self.n2 = Node([1, 3, 5], [150, 50], 25, [1, 2])
        self.n3 = Node([1, 2, 3], [150, 50], 25, [1, 3])


class test_basics(test_grid):

    def test_init(self):
        # test for initializing grid
        self.assertIsNotNone(self.g, 'Failed to initialize Grid.')

    def test_gameover(self):
        # game shouldn't be over at initialization
        expected = False
        actual = self.g.is_game_over()
        self.assertEqual(expected, actual)

    def test_getscore(self):
        # test getscore method at intialization
        expected = 0
        actual = self.g.get_score()
        self.assertEqual(expected, actual)

    def test_width(self):
        # test width initialization
        expected = 400
        actual = self.g._width
        self.assertEqual(expected, actual)

    def test_height(self):
        # test height initialization
        expected = 960
        actual = self.g._height
        self.assertEqual(expected, actual)

    def test_colour(self):
        # test colour initialization method
        expected = [1, 2, 3]
        actual = self.g.get_colour()
        self.assertEqual(expected, actual)

    def test_padding(self):
        # test padding initialization
        expected = 100
        actual = self.g._padding
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
