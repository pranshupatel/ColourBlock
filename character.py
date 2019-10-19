from typing import List, Dict, Tuple
class Character:
    
   """ CHARACTER CLASS
        This class represents a player in the game. It keeps track of the score and updates the score as the game is played.
        === Private Attributes ===
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
        

    
    
