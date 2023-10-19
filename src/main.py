"""Module to provide a text interface to the number guessing game"""
from game import Game
from player import Player


def input_integer(message: str, warning: str = "Please enter a valid integer. Try again.") -> int:
    """Safely read input and parse into integers"""
    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            print(warning)
    return number


def play() -> None:
    """User guesses the computer's number"""
    left = input_integer("Please enter the lower bound: ")
    right = input_integer("Please enter the upper bound: ")

    while right < left:
        right = input_integer("Upper bound must be greater or equal to lower bound! Try again.\
        \nPlease enter the upper bound: ")

    num = input_integer("Please enter a number to guess: ")

    game = Game(left, right)
    count: int = 1

    while game.guess(num) != 0:
        if count == 5:
            print("You already guessed 5 times! keep going!")
        elif count == 10:
            print("You already guessed 10 times! you are getting there!")

        if game.guess(num) == -1:
            print("You guessed too low!")
        else:
            print("You guessed too high!")

        count += 1
        num = input_integer("Please enter a number to guess: ")

    print("You won!")
    print("Took", round(game.get_time(), 2), "seconds")
    print("Took", count, "tries")


def guess() -> None:
    """Computer guesses the user's number"""
    player = Player()
    while not player.game_ended:
        print(f"Computer guessed {player.get_guess()}. (-1/0/1)")
        print("Enter -1 if the guess is too low")
        print("Enter 0 if the guess is correct")
        print("Enter 1 if the guess is too high")
        if not player.update(input_integer("Your answer:")):
            print("You sure? I think you made a mistake somewhere.")


def menu() -> None:
    """Display menu and handle user input"""
    Game.welcome()
    print("1. Play the game")
    print("2. Let the computer guess your number")
    print("3. Exit")

    while True:
        choice = input_integer("Please enter your choice: ")
        if choice == 1:
            play()
            break
        elif choice == 2:
            guess()
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice! Try again.")


def main():
    """Main function"""
    menu()


if __name__ == "__main__":
    main()
