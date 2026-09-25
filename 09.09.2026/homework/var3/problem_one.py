numbers: list[int] = []
multiplier1_query = ""
multiplier2_query = "\t"
n = 4

while n:
    try:
        num = int(input().strip())
        numbers.append(num)
        n -= 1
    except EOFError:
        break

multiplier1: list[int] = []
multiplier2: list[int] = []

for i in range(numbers[0], numbers[1] + 1):
    multiplier1.append(i)

for i in range(numbers[2], numbers[3] + 1):
    multiplier2.append(i)

multiplier2_query += "\t".join(str(n) for n in multiplier2)

print(multiplier2_query)

for i in multiplier1:
    print(f"\n{i}\t", end="")
    for x in multiplier2:
        print(f"{i * x}\t", end="")

print()
