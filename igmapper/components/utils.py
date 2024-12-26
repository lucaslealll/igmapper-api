import csv
from time import sleep

from tqdm import tqdm


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


def save_to_csv(file_name, data, headers):
    """Salva dados em um arquivo CSV."""
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)


def progress_bar(sec: int = 5, output: bool = True):
    "Barra de progresso... Defina os segundos"
    if output:
        for i in tqdm(range(sec), desc="Waiting..."):
            sleep(1)
    else:
        sleep(sec)
