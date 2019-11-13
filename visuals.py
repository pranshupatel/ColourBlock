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
        _player: the controller class this game is using
        _move_delay: the length of time between each user move
        _quick_drop: whether to drop the block quicker or normal speed
        _quick_drop_factor: how many times faster should the block fall when pressing down
    """

    _width: int
    _height: int
    _tick_length: int
    _font: str
    _player: None # By Default, will be type character if not None
    _move_delay: int
    _quick_drop: True
    _quick_drop_factor: int

    def __init__(self, width: int, height: int, tick: int, font: str, controller=None, move_delay=50, factor=8):
        """ Width, height, tick speed and font for the pygame window
            Controller refers to the character class if one is assinged
            This allows us to update the script of any user input

        """
        self._width = width
        self._height = height
        self._tick_length = tick
        self._font = font
        self._player = None
        if controller:
            self._player = controller
        self._move_delay = move_delay
        self._quick_drop = False
        self._quick_drop_factor = factor

    def play(self, grid: Grid) -> None:
        """ Set up a pygame window with the passed in grid """
        # Start pygame
        pygame.init()
        screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Colour Block")

        self.frame(screen, grid)
        self.end_game(grid)

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
            # pull from grid
            self.render_grid(screen, grid)            
            # go through all events on pygame
            keep_playing = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        actions = "left"
                    elif event.key == pygame.K_RIGHT:
                        actions = "right"
                    elif event.key == pygame.K_UP:
                        actions = "rotate"
                    if event.key == pygame.K_ESCAPE:
                        keep_playing = self.pause_game(screen)

                if event.type == pygame.QUIT or not keep_playing:
                    # user closed the window
                    print("user closed game")
                    # stop the game
                    pygame.quit()
                    return



            # check if user wants to increase block fall speed

            # tick len * 1 is normal
            speed_scale = 1

            pressed_keys = pygame.key.get_pressed()
            self._quick_drop = pressed_keys[pygame.K_DOWN]
            if self._quick_drop:
                # 1/2 * tick len means it comes up twice as often
                speed_scale = 1/self._quick_drop_factor          

            # execute player move
            if pygame.time.get_ticks() % self._move_delay == 0:
                # begin switch case
                if actions == "left":
                    self._player.play_move(-1)
                elif actions == "right":
                    self._player.play_move(1)
                elif actions == "rotate":
                    self._player.play_move(rotate=True)
                actions = "_"
            
            # Drop the block by 1 row
            if pygame.time.get_ticks() % (self._tick_length * speed_scale) == 0:
                
                # if the game is over do nothing
                if grid.is_game_over():
                    return

                # Move blocks down now that they have moved
                if self._player:
                    self._player.block_fall()

    def render_grid(self, screen: pygame.display, grid: Grid) -> None:
        """ Draw the grid on a pygame window
        """
        # reset the screen to black
        screen.fill((0,0,0))

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

    def pause_game(self, screen: pygame.display) -> bool:
        """ Pause the game until the user presses the resume key
            return true if user wants to resume, false if want to quit
        """
        print("game paused")

        # open menu
        surface = pygame.Surface((self._width, self._height))
        surface.set_alpha(128)
        surface.fill((84,89,97))

        screen.blit(surface, (0,0))

        # draw the text
        font = pygame.font.SysFont(self._font, 32)

        pause_text = font.render("paused", True, (255,255,255))
        text_rect = pause_text.get_rect()
        text_rect.center = (self._width // 2, self._height // 20)
        screen.blit(pause_text, text_rect)

        resume_text = font.render("press esc to resume", 32, (255,255,255))
        text_rect = resume_text.get_rect()
        text_rect.center = (self._width // 2, self._height // 7.5)
        screen.blit(resume_text, text_rect)
        
        # pygame.draw.rect(screen, (84,89,97, 5), (0,0, self._width, self._height))
        pygame.display.update()

        # pause the game
        while True:
            for event in pygame.event.get():
                # player wants to quit
                if event.type == pygame.QUIT:
                    return False
                # player wants to resume
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
    
    def end_game(self, grid: Grid) -> None:
        """ Run when the game is over
            Display the score
        """
        print("game is over")
        print("final score = ", grid.get_score())
        pygame.quit()
