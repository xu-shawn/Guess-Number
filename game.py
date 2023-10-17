import random


class Game:
    def __init__(self, low: int, high: int):
        self.number = random.randint(low, high)

    def guess(self, n: int):
        return 1 if n > self.number else (-1 if n < self.number else 0)
    
    def reset(self, low:int, high:int):
        self.number = random.randint(low, high)
