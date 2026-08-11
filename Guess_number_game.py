import random

jackpot = random.randint(1, 100)

guess = int(input("Guess a Number Between 1 and 100: "))
counter = 1

while guess != jackpot:

    if guess < jackpot:
        print("Too Low! Try Again")
    else:
        print("Too High! Try Again")

    guess = int(input("Guess a Number Between 1 and 100: "))
    counter += 1

print("Correct Guess! The Jackpot Number was", jackpot)
print("You took", counter, "Attempts.")