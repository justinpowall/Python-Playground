from .ui import header, divider, prompt, success, info


def run():
    header("👤  PERSONAL PROFILE")
    name  = prompt("What's your name?")
    age   = prompt("How old are you?")
    hobby = prompt("What's your favorite hobby?")

    try:
        years_to_100 = 100 - int(age)
    except ValueError:
        years_to_100 = "?"

    divider()
    info(f"Name    : {name}")
    info(f"Age     : {age}")
    info(f"Hobby   : {hobby}")
    success(f"Fun fact: ~{years_to_100} years until you're 100!")
    divider()
