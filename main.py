import game
print("Welcome to the guessing game! All number must be integers.")
l=int(input("Please enter a lower bound: "))
r=int(input("Please enter an upper bound: "))
game = game.Game(l,r)
num = int(input("Please enter a number to guess: "))
while game.guess(num) != 0:
    if (game.guess(num) == -1):
        print("You guessed too low!")
    else:
        print("You guessed too high!")
    num = int(input("Please enter a number to guess: "))
print("You win the game!")
