"""Задача Дважды Три"""

number = int(input())


def ternary(num: int) -> int:
    if num == 0:
        return 0
    s = ""
    while num:
        s += str(num % 3) + str(num % 3)
        num //= 3
    encoded = s[::-1]
    return int(encoded, 3)


print(ternary(number))
