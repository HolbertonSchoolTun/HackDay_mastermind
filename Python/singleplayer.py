#!/usr/bin/python3
"""
The single player virsion of the game
"""
import random
from mastermind import Mastermind
class SinglePlayer(Mastermind):
    """
    Full the list objictive with random numbers
    """
    def __init__(self):
        """
        inisialise objictive
        """
        self.objective = SinglePlayer.randomize()
    def randomize():
        """
        full the objictive with random numbers./t   
        """
        objective = []
        for i in range(4):
            objective.append(random.randint(1, 6))
        return (objective)



