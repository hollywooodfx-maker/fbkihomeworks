"""Задача Класс"""

# Обьявление множества для хранения точек
dots = set()
# Обьявление множества уже посещенных точек
seen = set()
# Обьявление счетчика цветов
color_count = 0

# Чтение чисел из потока stdin
while True:
    try:
        # [int(x), int(y)]
        x, y = map(int, input().split())
        dots.add(
            (
                x,
                y,
            )
        )
        # EndOfFile
    except EOFError:
        break

# Итерация по парам точек
for dot in dots:
    # Если точка уже найдена и была проверена
    if dot in seen:
        # пропускаем
        continue
    # Запоминаем точку
    seen.add(dot)
    # Новая пара или одиночная точка
    color_count += 1
    # Лист для поиска подходящих точек в пару
    search = [dot]

    while search:
        # берем первую точку (x, y)
        x, y = search.pop(0)
        # Те точки, что подходят по условию
        approved_dots = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        for dot in approved_dots:
            # Если точка есть в файле и она не была проверена
            if (dot in dots) and (dot not in seen):
                seen.add(dot)
                # Следующая на поиск пары точка
                search.append(dot)

print(color_count)
