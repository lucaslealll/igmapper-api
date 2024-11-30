def bold_str(text):
    return f"\033[1m{text}\033[0m"


def green_str(text):
    return f"\033[32m{text}\033[0m"


def italic_str(text):
    return f"\033[3m{text}\033[0m"


def red_str(text):
    return f"\033[31m{text}\033[0m"


def reset_color_str(text):
    return f"\033[0m{text}"


def strikethrough_str(text):
    return f"\033[9m{text}\033[0m"


def underline_str(text):
    return f"\033[4m{text}\033[0m"
