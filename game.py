import random

class Game:
    def __init__(self):
        self.number = random.randint(0, 1000)
    def guess(self, n: int):
        return 1 if n > self.number else (-1 if n < self.number else 0)