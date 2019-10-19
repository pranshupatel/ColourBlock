from typing import List, Dict, Tuple
class Character:
    
   """ CHARACTER CLASS
        This class is a 20 x 10 list of nodes, to be displayed to the screen
        === Private Variables ===
        _name - The name of the character.
        _time - The amount of seconds the character has been in the game.
        _score = The current score of the player.
    """
    _name: str
    _time: int
    _score: int
    
    def __init__ (self, name: str, time: int):
        """Initialize the new character entering the game.
        """
        self._name = name
        self._time = time
        self._score = 0

    
    
