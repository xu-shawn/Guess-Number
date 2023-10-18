"""Module providing a number guessing game"""
import random
import time


class Game:
    """Class representing a number gussing game"""

    def __init__(self, low: int, high: int):
        self.number = random.randint(low, high)
        self.start_time = time.time()

    def guess(self, n: int) -> int:
        """Function to check if a guess is correct"""
        return 1 if n > self.number else (-1 if n < self.number else 0)

    def get_time(self) -> float:
        """Function to get the number of seconds that has elapsed since the last reset"""
        return time.time() - self.start_time

    def reset(self, low: int, high: int) -> None:
        """Function to reset the number to be guessed"""
        self.number = random.randint(low, high)
        self.start_time = time.time()

    @staticmethod
    def welcome() -> None:
        """Function to print a welcome message"""
        print(r"__        __   _                            _          _   _            ")
        print(r"\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___   ")
        print(r" \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \  ")
        print(r"  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/  ")
        print(r"   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|_ ")
        print(r"  __ _ _   _  ___  ___ ___(_)_ __   __ _    __ _  __ _ _ __ ___   ___| |")
        print(r" / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \ |")
        print(r"| (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/_|")
        print(r" \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___(_)")
        print(r" |___/                             |___/   |___/                        ")
