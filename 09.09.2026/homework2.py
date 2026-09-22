"""Задача Тьюринг"""

array = []

# array = [
#   [r,r,d,l],
#   [u,r,d,l],
#   [d,d,r,l],
#   [l,d,r,l]
# ]

while True:
    try:
        array.append(list(input()))
    except EOFError:
        break


def find_cicle() -> str:
    index = []
    current_point = (0, 0)
    x = y = 0
    while current_point not in index:
        index.append(current_point)
        if array[y][x] == "r":
            if x + 1 > (len(array) - 1):
                current_point = (y, 0)
            else:
                current_point = (y, x + 1)
            y, x = current_point
        elif array[y][x] == "l":
            if x - 1 < 0:
                current_point = (y, (len(array) - 1))
            else:
                current_point = (y, x - 1)
            y, x = current_point
        elif array[y][x] == "u":
            if y - 1 < 0:
                current_point = ((len(array) - 1), x)
            else:
                current_point = (y - 1, x)
            y, x = current_point
        elif array[y][x] == "d":
            if y + 1 > (len(array) - 1):
                current_point = (0, x)
            else:
                current_point = (y + 1, x)
            y, x = current_point
    return f"{current_point[1]} {current_point[0]}"


print(find_cicle())
