""" This class is meant to display the game to the player

    In MCV model, this is the VIEW

    Author: Ajitesh Misra
"""

from typing import List, Dict, Tuple
import pygame
from grid import Grid
from node import Node

""" === CONSTANTS === """
ORIGIN = (0, 0)

""" === Resolution === """
WIDTH = 1024
HEIGHT = 768

""" === FONT === """
FONT = 'Consolas'

""" === CLOCK SPEED """
TICK_LENGTH = 500

class Visuals:

    def Visuals(self):
        """ There are no needed variables for this class
        """
        pass

    def play(self, grid: Grid):
        """ Set up a pygame window with the passed in grid """
        # Start pygame
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Colour Block")

        colour = (0, 32, 64)
        padding = 1

        # to centre, take centre of screen then subtract the grid's width (which is HEIGHT // 2)
        left_offset = (WIDTH - (HEIGHT // 2)) // 2

        print(left_offset)

        self.frame(screen, grid)


    def frame(self, screen: pygame.display , grid: Grid):
        """ Runs every frame of the game

            Takes in a grid to display
        """
        print("frame 0")

        while(True):
            pygame.time.delay(TICK_LENGTH)
            print("tick")
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

if __name__ == "__main__":
    left_offset = (WIDTH - (HEIGHT // 2)) // 2
    grid = Grid(WIDTH, HEIGHT, 1, (0,32,64), left_offset)
    
    v = Visuals()
    v.play(grid)