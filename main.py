"""Module to provide a text interface to the number guessing game"""
import time
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
t1 = time.time()
game = game.Game(l, r)
num = int(input("Please enter a number to guess: "))
count: int = 1

while game.guess(num) != 0:
    if game.guess(num) == -1:
        print("You guessed too low!")
    else:
        print("You guessed too high!")
    count += 1
    if count==5:
        print("You already guessed 5 times! keep going!")
    if count==10:
        print("You already guessed 10 times! you are getting there!")
    num = int(input("Please enter a number to guess: "))

t2 = time.time()
print("You win the game!")
print("Time taken: ", round(t2 - t1, 2), " seconds")
print("Number of guesses: ", count)
    while game.guess(num) != 0:
        if game.guess(num) == -1:
            print("You guessed too low!")
        else:
            print("You guessed too high!")
        count += 1
        num = input_integer("Please enter a number to guess: ")

    print("You won!")
    print("Took", round(game.get_time(), 2), "seconds")
    print("Took", count, "tries")


if __name__ == "__main__":
    main()
