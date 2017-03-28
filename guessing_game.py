import random

secret = random.randrange(1, 101)
print(secret)

while guess != secret:
    guess = int(input)"Make a guess"
    tries = tries + 1

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print ("Too Low")
