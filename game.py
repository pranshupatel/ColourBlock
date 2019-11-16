from player import Player

"""
Create a new game of Colour Block
"""

def play():
    """ Create a new game of colour block, and 
        make a new window when the player restarts
    """
    while True:
        player = Player("name", 1)

        # if here player has lost the game or quit
        if player.has_quit():
            break

        print("GAME OVER")


if __name__ == "__main__":
    play()