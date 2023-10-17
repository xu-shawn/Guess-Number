"""Module providing the number guessing game"""
import game

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
print("All number must be integers.")

l = int(input("Please enter a lower bound: "))
r = int(input("Please enter an upper bound: "))
game = game.Game(l, r)
num = int(input("Please enter a number to guess: "))

while game.guess(num) != 0:

    if game.guess(num) == -1:
        print("You guessed too low!")

    else:
        print("You guessed too high!")

    num = int(input("Please enter a number to guess: "))

print("You win the game!")
