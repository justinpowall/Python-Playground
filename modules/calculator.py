from .ui import header, divider, prompt, success, error, info


def run():
    header("🔢  MINI CALCULATOR")
    info("Supports: + - * / ^ and parentheses")
    divider()
    expr = prompt("Expression:").replace("^", "**")
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        success(f"Result: {result}")
    except Exception as e:
        error(f"Couldn't compute that ({e})")
    divider()
