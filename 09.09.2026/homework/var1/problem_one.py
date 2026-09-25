summary = 0
var = 0

while True:
    try:
        num = int(input().strip())
        summary += num ** 2
        var += num
    except EOFError:
        break
    if var == 0:
        break

print(summary)
