from modules import profile, number_games, word_tools, calculator, trivia, dice
from modules.ui import c, error, CYAN, MAGENTA, YELLOW, GREEN, BOLD, DIM


MODULES = {
    "1": ("Personal Profile",  "👤", profile),
    "2": ("Number Games",      "🎲", number_games),
    "3": ("Word Tools",        "📝", word_tools),
    "4": ("Mini Calculator",   "🔢", calculator),
    "5": ("Trivia Quiz",       "🧠", trivia),
    "6": ("Dice & Coin",       "🎯", dice),
}


def banner():
    print()
    print(c("  ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗  ██╗", CYAN, BOLD))
    print(c("  ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗ ██║", CYAN, BOLD))
    print(c("  ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗██║", CYAN, BOLD))
    print(c("  ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚████║", CYAN, BOLD))
    print(c("  ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚███║", CYAN, BOLD))
    print(c("  ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝", CYAN, BOLD))
    print()
    print(c("         P L A Y G R O U N D   v 1 . 0", DIM))
    print()


def menu():
    print(c("  ╔══════════════════════════════════════════╗", MAGENTA))
    print(c("  ║           WHAT DO YOU WANT TO DO?        ║", MAGENTA, BOLD))
    print(c("  ╠══════════════════════════════════════════╣", MAGENTA))
    for key, (label, icon, _) in MODULES.items():
        key_str = c(f" [{key}]", YELLOW, BOLD)
        print(f"  {c('║', MAGENTA)}  {key_str}  {icon}  {label:<22}{c('║', MAGENTA)}")
    print(c("  ╠══════════════════════════════════════════╣", MAGENTA))
    quit_str = c(" [q]", YELLOW, BOLD)
    print(f"  {c('║', MAGENTA)}  {quit_str}  ✖  {'Quit':<26}{c('║', MAGENTA)}")
    print(c("  ╚══════════════════════════════════════════╝", MAGENTA))
    return input(c("\n  › ", YELLOW, BOLD)).strip().lower()


def main():
    banner()
    while True:
        choice = menu()
        print()
        if choice in MODULES:
            _, _, mod = MODULES[choice]
            try:
                mod.run()
            except KeyboardInterrupt:
                print(c("\n\n  Cancelled.", DIM))
            except Exception as e:
                error(f"Module crashed: {e}")
        elif choice == "q":
            print()
            print(c("  Later! Keep coding. 👋\n", GREEN, BOLD))
            break
        else:
            print(c("  Invalid option, try again.", DIM))


main()
