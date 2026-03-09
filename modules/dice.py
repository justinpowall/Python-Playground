import random
from .ui import header, divider, prompt, success, info, error


def run():
    header("🎯  DICE & COIN")
    info("Flip a coin or roll dice.")
    divider()

    choice = prompt("Flip coin [c] or roll dice [d]?").lower()

    if choice == "c":
        result = random.choice(["Heads", "Tails"])
        icon = "🟡" if result == "Heads" else "⚫"
        success(f"{icon}  {result}!")

    elif choice == "d":
        sides_input = prompt("How many sides? (default 6)")
        try:
            sides = int(sides_input) if sides_input else 6
            if sides < 2:
                raise ValueError
        except ValueError:
            error("Invalid number of sides.")
            return

        count_input = prompt("How many dice? (default 1)")
        try:
            count = int(count_input) if count_input else 1
            if count < 1 or count > 20:
                raise ValueError
        except ValueError:
            error("Please enter between 1 and 20 dice.")
            return

        rolls = [random.randint(1, sides) for _ in range(count)]
        success(f"Rolled: {rolls}")
        if count > 1:
            info(f"Total: {sum(rolls)}")

    else:
        error("Unknown option.")

    divider()
