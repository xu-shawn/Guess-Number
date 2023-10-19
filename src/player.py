"""Module to represent a computer player"""


class Player:
    """Class representing a player"""
    def __init__(self) -> None:
        self.max: int = None
        self.min: int = None
        self.extreme: int = None
        self.last_guess: int = None
        self.game_ended: bool = False

    def get_guess(self) -> int:
        """Returns the optimal guess using known information."""
        if self.extreme is None:
            self.last_guess = 0
            return 0
        elif self.min is None or self.max is None:
            self.last_guess = self.extreme
            return self.last_guess
        else:
            self.last_guess = (self.max + self.min) // 2
            return self.last_guess

    def update(self, result: int) -> bool:
        """Updates the player using the result of the last guess

        Parameter:
            result (int): A negative integer, zero, or a positive integer
            as the last guess is less than, equal to, or greater than the actual value

        Returns:
            A boolean value indicating the validity of the result
        """

        if result < 0:
            return self._update_negative()

        if result > 0:
            return self._update_positive()

        self.gameover()
        return True

    def _update_negative(self) -> bool:
        """Helper function to handel the result < 0 case for function update()"""
        if self.extreme is None:
            self.extreme = 1
            self.min = 1
        elif self.min is None or self.max is None:
            if self.extreme < 0:
                self.min = self.last_guess + 1
            else:
                self.min = self.extreme + 1
                self.extreme = self.extreme * 2
        else:
            if self.last_guess >= self.max:
                return False
            self.min = self.last_guess + 1
        return True

    def _update_positive(self) -> bool:
        """Helper function to handel the result > 0 case for function update()"""
        if self.extreme is None:
            self.extreme = -1
            self.max = -1
        elif self.min is None or self.max is None:
            if self.extreme < 0:
                self.max = self.extreme - 1
                self.extreme *= 2
            else:
                self.max = self.last_guess - 1
        else:
            if self.last_guess <= self.min:
                return False
            self.max = self.last_guess - 1
        return True

    def gameover(self) -> None:
        """Prints a message after game has ended"""
        print("Game Over")
        self.game_ended = True
