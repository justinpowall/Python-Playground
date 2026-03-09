# ANSI color/style helpers

RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"


def c(text, *styles):
    """Wrap text in ANSI styles."""
    return "".join(styles) + str(text) + RESET


def header(title):
    width = 42
    print()
    print(c("╔" + "═" * width + "╗", CYAN, BOLD))
    print(c("║" + title.center(width) + "║", CYAN, BOLD))
    print(c("╚" + "═" * width + "╝", CYAN, BOLD))
    print()


def divider():
    print(c("  " + "─" * 38, DIM))


def success(msg):
    print(c(f"  ✔  {msg}", GREEN, BOLD))


def error(msg):
    print(c(f"  ✘  {msg}", RED, BOLD))


def info(msg):
    print(c(f"  ●  {msg}", CYAN))


def prompt(msg):
    return input(c(f"  {msg} ", YELLOW, BOLD))


def option_prompt():
    return input(c("\n  › ", MAGENTA, BOLD)).strip().lower()
