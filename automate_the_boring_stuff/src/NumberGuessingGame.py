import random

number = random.randint(1,20)
guess_count = 0

print("I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    guess_count += 1

    if guess == number:
        print("Good job! You guessed my number in {} guesses!".format(guess_count))
        break
    elif guess > number:
        print("Your guess is too high.")
        continue
    elif guess < number:
        print("Your guess is too low.")
        continue
