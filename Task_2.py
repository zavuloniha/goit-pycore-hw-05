import re
from typing import Callable


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід," \
       "доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    pattern = r"\s+\d+\.+\d+\s"
    match = re.findall(pattern, text)
    for item in match:
        number = float(item)
        yield number


def sum_profit(text: str, func: Callable):
    total_sum = 0
    for number in func(text):
        total_sum += number   
    return total_sum


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
