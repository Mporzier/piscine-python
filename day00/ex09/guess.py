import sys
import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
number = random.randint(1, 99)
guess = ''
result = 0
i = 0
while 1:
    print("What's your guess between 1 and 99?")
    print(">> ", end='')
    guess = input()
    if guess == 'exit':
        print("Goodbye!")
        sys.exit()
    if not guess.isdigit():
        print("That's not a number.")
    else:
        result = int(guess)
    i += 1
    if result == number:
        break
    elif result < number:
        print("Too low!")
    elif result > number:
        print("Too high!")

if number == 42:
    print("The answer is the ultimate question of life, the universe and everything is 42.")
if i == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you got it!")
    print("You won in", i, "attempts!")
