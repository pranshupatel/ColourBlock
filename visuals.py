""" This class is meant to display the game to the player

    In MCV model, this is the VIEW

    Author: Ajitesh Misra
"""

from typing import List, Dict, Tuple
import pygame
from grid import Grid
from node import Node

# """ === CONSTANTS === """
# ORIGIN = (0, 0)

# """ === Resolution === """
# WIDTH = 1024
# HEIGHT = 768

# """ === FONT === """
# FONT = 'Consolas'

# """ === CLOCK SPEED """
# TICK_LENGTH = 500

class Visuals:
    """ This class is the front end of the game
        It is meant to be able to take in a grid and render it 


        === PRIVATES ===
        _width: the width of the window in PIXELS
        _height: the height of the window in PIXELS
        _tick_lenth: the ms between each update
        _font: the font to use in pygame
    """

    _width: int
    _height: int
    _tick_length: int
    _font: str

    def __init__(self, width: int, height: int, tick: int, font: str):
        """ There are no needed variables for this class
        """
        self._width = width
        self._height = height
        self._tick_length = tick
        self._font = font

    def play(self, grid: Grid):
        """ Set up a pygame window with the passed in grid """
        # Start pygame
        pygame.init()
        screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Colour Block")

        # colour = (0, 32, 64)
        # padding = 1

        # to centre, take centre of screen then subtract the grid's width (which is HEIGHT // 2)
        left_offset = (self._width - (self._height // 2)) // 2

        # print(left_offset)

        self.frame(screen, grid)

    def update_tick(self, new_tick:int):
        """ Update the tick length to the new tick length
        """
        self._tick_length = new_tick

    def frame(self, screen: pygame.display , grid: Grid):
        """ Runs every frame of the game

            Takes in a grid to display
        """
        print("frame 0")

        while(True):
            # timer for when to update
            pygame.time.delay(self._tick_length)
            
            # pull from grid
            self.render_grid(screen, grid)
            for event in pygame.event.get():
                # go through all events on pygame
                if event.type == pygame.QUIT:
                    # user closed the window
                    print("user closed game")
                    # stop the game
                    pygame.quit()
                    exit()

    def render_grid(self, screen: pygame.display, grid: Grid):
        """ Draw the grid on a pygame window
        """
        nodes = grid.get_nodes()
        for line in nodes:
            for node in line:
                pos = node.get_position()
                colour = node.get_colour()
                length = node.get_length()

                pygame.draw.rect(screen, colour, (pos[0], pos[1], length, length))
        pygame.display.update()
