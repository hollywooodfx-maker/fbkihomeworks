numbers: dict[str, int] = {}
char = ["a", "b", "c", "d", "e"]

while char:
    try:
        num = int(input().strip())
        numbers[char.pop(0)] = num
    except EOFError:
        break


def find_solutions(a: int, b: int, c: int, d: int, e: int) -> int:
    cnt = 0

    def equation(x: int) -> None:
        nonlocal cnt
        if x == e:
            return
        eq = a * (x**3) + b * (x**2) + c * x + d
        if eq == 0:
            cnt += 1

    for x in range(1001):
        equation(x)
    return cnt


print(find_solutions(**numbers))
