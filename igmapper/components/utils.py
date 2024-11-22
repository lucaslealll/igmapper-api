def bold(text):
    return f"\033[1m{text}\033[0m"


def italic(text):
    return f"\033[3m{text}\033[0m"


def underline(text):
    return f"\033[4m{text}\033[0m"


def strikethrough(text):
    return f"\033[9m{text}\033[0m"


def reset_color(text):
    return f"\033[0m{text}"


def green(text):
    return f"\033[32m{text}\033[0m"


def red(text):
    return f"\033[31m{text}\033[0m"
