"""Module providing a number guessing game"""
import random


class Game:
    """Class representing a number gussing game"""

    def __init__(self, low: int, high: int):
        self.number = random.randint(low, high)

    def guess(self, n: int) -> int:
        """Function to check if a guess is correct"""
        return 1 if n > self.number else (-1 if n < self.number else 0)

    def reset(self, low: int, high: int) -> None:
        """Function to reset the number to be guessed"""
        self.number = random.randint(low, high)
