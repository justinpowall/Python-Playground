import random
import time
from .ui import header, divider, prompt, success, error, info, c, YELLOW, BOLD, GREEN, RED, CYAN


QUESTIONS = [
    ("What is 12 * 12?", "144"),
    ("What language are we programming in?", "python"),
    ("How many sides does a hexagon have?", "6"),
    ("What is the capital of France?", "paris"),
    ("What does CPU stand for? (3 words)", "central processing unit"),
]


def run():
    header("🧠  TRIVIA QUIZ")
    info("5 questions. Answer carefully!\n")
    divider()

    score = 0
    questions = QUESTIONS[:]
    random.shuffle(questions)

    for i, (q, a) in enumerate(questions, 1):
        print(c(f"  Q{i}: {q}", YELLOW, BOLD))
        answer = prompt("›").strip().lower()
        if answer == a.lower():
            success("Correct!")
        else:
            error(f"Wrong! Answer: {a}")
        print()
        time.sleep(0.3)
        score += answer == a.lower()

    divider()
    print(c(f"  Final Score: {score}/{len(questions)}", CYAN, BOLD))
    if score == len(questions):
        success("Perfect score! You're a genius.")
    elif score >= 3:
        success("Nice job!")
    else:
        error("Better luck next time!")
    divider()
