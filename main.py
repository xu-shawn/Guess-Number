"""Module to provide a text interface to the number guessing game"""
from game import Game


def input_integer(message: str, warning: str = "Please enter an integer. Try again.") -> int:
    """Safely read input and parse into integers"""
    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            print(warning)
    return number


def main() -> None:
    """Main function"""
    Game.welcome()

    l = input_integer("Please enter a lower bound: ")
    r = input_integer("Please enter an upper bound: ")
    num = input_integer("Please enter a number to guess: ")

    game = Game(l, r)
    count: int = 1

    while game.guess(num) != 0:
        if game.guess(num) == -1:
            print("You guessed too low!")
        else:
            print("You guessed too high!")
        count += 1
        num = input_integer("Please enter a number to guess: ")

    print("You win the game!")
    print("Time taken: ", round(game.get_time(), 2), " seconds")
    print("Number of guesses: ", count)


if __name__ == "__main__":
    main()
