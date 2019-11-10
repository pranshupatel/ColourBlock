"""Author: Yan Chen (Ryan) Huang"""

from grid import *
import unittest
from node import *


class test_node(unittest.TestCase):
    """setup the node for testing
    """
    def setUp(self):
        self.n = Node([1, 2, 3], [100, 200], 5, [50, 80])


class test_basics(test_node):

    def test_init(self):
        """ test for initializing node
        """
        self.assertIsNotNone(self.n, 'Failed to initialize Grid.')

    def test_colour_init(self):
        """ test for initializing colour
        """
        expected = [1, 2, 3]
        actual = self.n.colour
        self.assertEqual(expected, actual)

    def test_background_colour(self):
        """ test for initializing background colour (same as colour)
        """
        expected = [1, 2, 3]
        actual = self.n._background_colour
        self.assertEqual(expected, actual)

    def test_position_init(self):
        """ test for initializing position
        """
        expected = [100, 200]
        actual = self.n._position
        self.assertEqual(expected, actual)

    def test_coords_init(self):
        """ test for initializing coords
        """
        expected = [50, 80]
        actual = self.n._coords
        self.assertEqual(expected, actual)


class test_methods(test_node):
    def test_getpos(self):
        """ test for getting current position
        """
        expected = [100, 200]
        actual = self.n.get_position()
        self.assertEqual(expected, actual)

    def test_getcoords(self):
        """ test for getting current coords
        """
        expected = [50, 80]
        actual = self.n.get_coords()
        self.assertEqual(expected, actual)

    def test_getcolour(self):
        """ test for getting colour
        """
        expected = [1, 2, 3]
        actual = self.n.get_colour()
        self.assertEqual(expected, actual)

    def test_getlength(self):
        """ test for getting length
        """
        expected = 5
        actual = self.n.get_length()
        self.assertEqual(expected, actual)

    def test_initial_control(self):
        """ test for incontrol initialization
        """
        expected = False
        actual = self.n.get_in_control()
        self.assertEqual(expected, actual)

    def test_initial_filled(self):
        """ test for filled initialization
        """
        expected = False
        actual = self.n.get_filled()
        self.assertEqual(expected, actual)

    def test_set_colour(self):
        """ test for setting colour
        """
        expected = [10, 15, 20]
        self.n.set_colour([10, 15, 20])
        actual = self.n.colour
        self.assertEqual(expected, actual)

    def test_set_colour2(self):
        """ test for setting colour a second time
        """
        expected = [0, 0, 0]
        self.n.set_colour([10, 15, 20])
        self.n.set_colour([0, 0, 0])
        actual = self.n.colour
        self.assertEqual(expected, actual)

    def test_reset_colour(self):
        """ test for resetting colour
        """
        expected = self.n._background_colour
        self.n.reset_colour()
        actual = self.n.colour
        self.assertEqual(expected, actual)

    def test_setcontrol(self):
        """ test for setting incontrol
        """
        expected = True
        self.n.set_control(True)
        actual = self.n._in_control
        self.assertEqual(expected, actual)

    def set_filled(self):
        """ test for setting filled
        """
        expected = True
        self.n.set_filled(True)
        actual = self.n._filled
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main(exit=False)
