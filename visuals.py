""" This class is meant to display the game to the player

    In MCV model, this is the VIEW

    Author: Ajitesh Misra
"""

from typing import List, Dict, Tuple
import pygame
from grid import Grid
from node import Node

class Visuals:
    """ This class is the front end of the game
        It is meant to be able to take in a grid and render it 


        === PRIVATES ===
        _width: the width of the window in PIXELS
        _height: the height of the window in PIXELS
        _tick_lenth: the ms between each update
        _font: the font to use in pygame
        _char: the character class this game is using
        _move_delay: the length of time between each user move
    """

    _width: int
    _height: int
    _tick_length: int
    _font: str
    _char: None # By Default, will be type character if not None
    _move_delay: int

    def __init__(self, width: int, height: int, tick: int, font: str, controller=None, move_delay=50):
        """ Width, height, tick speed and font for the pygame window
            Controller refers to the character class if one is assinged
            This allows us to update the script of any user input

        """
        self._width = width
        self._height = height
        self._tick_length = tick
        self._font = font
        self._char = None
        if controller:
            self._char = controller
        self._move_delay = move_delay

    def play(self, grid: Grid) -> None:
        """ Set up a pygame window with the passed in grid """
        # Start pygame
        pygame.init()
        screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Colour Block")

        self.frame(screen, grid)

    def update_tick(self, new_tick:int) -> None:
        """ Update the tick length to the new tick length
        """
        self._tick_length = new_tick

    def frame(self, screen: pygame.display , grid: Grid) -> None:
        """ Runs every frame of the game

            Takes in a grid to display
        """

        # store ref for what action to take next tick
        actions = "_"

        while(True):
            # timer for when to update
            # pygame.time.delay(self._tick_length)
            
            # pull from grid
            self.render_grid(screen, grid)

            # go through all events on pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # user closed the window
                    print("user closed game")
                    # stop the game
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        actions = "left"
                    elif event.key == pygame.K_RIGHT:
                        actions = "right"
                    elif event.key == pygame.K_UP:
                        actions = "rotate"
                    elif event.key == pygame.K_DOWN:
                        actions = "down"

            # Drop the block by 1 row
            if pygame.time.get_ticks() % self._tick_length == 0:

                # Move blocks down now that they have moved
                if self._char:
                    self._char.block_fall()

            # execute player move
            if pygame.time.get_ticks() % self._move_delay == 0:
                print(actions)
                # begin switch case
                if actions == "left":
                    self._char.play_move(-1)
                elif actions == "right":
                    self._char.play_move(1)
                elif actions == "rotate":
                    self._char.play_move(rotate=True)
                elif actions == "down":
                    self._char.play_move(speed_down=True)
                actions = "_"

    def render_grid(self, screen: pygame.display, grid: Grid) -> None:
        """ Draw the grid on a pygame window
        """
        nodes = grid.get_nodes()

        # NOTE: Render only the bottom 20 
        #       This is so new blocks can be spawned 
        #       Out of the players view
        for line in nodes[4:]:
            for node in line:
                pos = node.get_position()
                colour = node.get_colour()
                length = node.get_length()

                pygame.draw.rect(screen, colour, (pos[0], pos[1], length, length))
        pygame.display.update()
