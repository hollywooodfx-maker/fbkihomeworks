from typing import Optional


numbers: dict[str, int] = {}
char = [
    "a",
    "b",
    "c",
    "d",
]
while char:
    try:
        num = int(input().strip())
        numbers[char.pop(0)] = num
    except EOFError:
        break


def find_solutions(a: int, b: int, c: int, d: int) -> Optional[list[int]]:
    solutions = []

    def equation(x: int) -> None:
        nonlocal solutions
        eq = a * (x**3) + b * (x**2) + c * x + d
        if eq == 0:
            solutions.append(x)

    for x in range(1001):
        equation(x)
    return solutions[::-1] if solutions else None


if solutions := find_solutions(**numbers):
    print(*solutions)
