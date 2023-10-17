import game
game = game.Game()

print("Welcome to the guessing game!")
num = int(input("Please enter a number: "))
while game.guess(num) != 0:
    if (game.guess(num) == -1):
        print("You guessed too low!")
    else:
        print("You guessed too high!")
    num = int(input("Please enter a number: "))
print("You win the game!")
