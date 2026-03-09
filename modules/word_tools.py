from .ui import header, divider, prompt, success, error, info, option_prompt, c, YELLOW, GREEN, RED, CYAN, BOLD


def run():
    header("📝  WORD TOOLS")
    print(c("  [a]  Reverse a word", YELLOW))
    print(c("  [b]  Count letters", YELLOW))
    print(c("  [c]  Palindrome check", YELLOW))
    choice = option_prompt()
    word = prompt("Enter a word or sentence:")

    if choice == "a":
        info(f"Reversed: {word[::-1]}")
    elif choice == "b":
        _letter_count(word)
    elif choice == "c":
        _palindrome(word)
    else:
        error("Invalid option.")
    divider()


def _letter_count(word):
    counts = {}
    for ch in word.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
    divider()
    print(c("  Letter counts:", CYAN, BOLD))
    for letter, count in sorted_counts:
        bar = c("█" * count, GREEN)
        print(f"    {c(letter, YELLOW, BOLD)}  {bar}  {count}")


def _palindrome(word):
    cleaned = word.lower().replace(" ", "")
    divider()
    if cleaned == cleaned[::-1]:
        success(f'"{word}" IS a palindrome!')
    else:
        error(f'"{word}" is NOT a palindrome.')
