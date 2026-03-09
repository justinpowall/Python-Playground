import random
import math
from .ui import header, divider, prompt, success, error, info, option_prompt, c, YELLOW, BOLD


def run():
    header("🎲  NUMBER GAMES")
    print(c("  [a]  Guess the number", YELLOW))
    print(c("  [b]  Is it prime?", YELLOW))
    choice = option_prompt()

    if choice == "a":
        _guess_the_number()
    elif choice == "b":
        _prime_check()
    else:
        error("Invalid option.")


def _guess_the_number():
    secret = random.randint(1, 20)
    attempts = 0
    divider()
    info("I'm thinking of a number between 1 and 20...")
    while True:
        guess = prompt("Your guess:")
        try:
            guess = int(guess)
            attempts += 1
            if guess < secret:
                print(c("  ↑  Too low!", YELLOW, BOLD))
            elif guess > secret:
                print(c("  ↓  Too high!", YELLOW, BOLD))
            else:
                success(f"Correct! You got it in {attempts} attempt(s)!")
                break
        except ValueError:
            error("Enter a valid number.")
    divider()


def _prime_check():
    divider()
    num = prompt("Enter a number:")
    try:
        num = int(num)
        if num < 2:
            error(f"{num} is not a prime number.")
        elif all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            success(f"{num} IS a prime number!")
        else:
            error(f"{num} is NOT a prime number.")
    except ValueError:
        error("That's not a valid number.")
    divider()
