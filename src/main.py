"""Module to provide a text interface to the number guessing game"""
import os
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
            print("You've already guessed 5 times! keep going!")
        elif count == 10:
            print("You've already guessed 10 times! you are getting there!")

        if game.guess(num) == -1:
            print("You guessed too low!")
        else:
            print("You guessed too high!")

        count += 1
        num = input_integer("Please enter a number to guess: ")

    print("You won!")
    print(f"Took {round(game.get_time(), 2)} seconds")
    print(f"Took {count} tries")


def guess() -> None:
    """Computer guesses the user's number"""
    player = Player()
    count: int = 0
    while not player.game_ended:
        print(f"Computer guessed {player.get_guess()}. (-1/0/1)")
        count += 1
        print("Enter 1 if the answer is too low")
        print("Enter 0 if the answer is correct")
        print("Enter -1 if the answer is too high")
        if not player.update(-input_integer("Your answer: ")):
            print("Are you sure? I think you made a mistake somewhere.")
            player.min = input_integer("Please enter lower bound: ")
            player.max = input_integer("Please enter upper bound: ")

            while player.min > player.max:
                print("Please make sure that the bounds are valid!")               
                player.min = input_integer("Please re-enter lower bound: ")
                player.max = input_integer("Please re-enter upper bound: ")
    print(f"Took {count} tries" if count != 1 else "Took 1 try")



def menu() -> None:
    """Display menu and handle user input"""
    while True:
        Game.welcome()
        print("1. Play the game")
        print("2. Let the computer guess your number")
        print("3. Exit")

        choice = input_integer("Please enter your choice: ")

        if choice == 1:
            os.system("clear")
            play()
            input("Press Enter to continue...")
            os.system("clear")
            continue

        if choice == 2:
            os.system("clear")
            guess()
            input("Press Enter to continue...")
            os.system("clear")
            continue

        if choice == 3:
            break

        os.system("clear")
        print("Invalid choice! Try again.")
        input("Press Enter to continue...")


def main():
    """Main function"""
    menu()


if __name__ == "__main__":
    main()
