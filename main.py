"""Module to provide a text interface to the number guessing game"""
from game import Game

def main() -> None:
    """Main function"""
    Game.welcome()

    l = int(input("Please enter a lower bound: "))
    r = int(input("Please enter an upper bound: "))
    num = int(input("Please enter a number to guess: "))

    game = Game(l, r)
    count: int = 1

    while game.guess(num) != 0:
        if game.guess(num) == -1:
            print("You guessed too low!")
        else:
            print("You guessed too high!")
        count += 1
        num = int(input("Please enter a number to guess: "))

    print("You win the game!")
    print("Time taken: ", round(game.get_time(), 2), " seconds")
    print("Number of guesses: ", count)

if __name__ == "__main__":
    main()
