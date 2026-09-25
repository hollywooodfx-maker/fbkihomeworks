num = int(input().strip())

s = ""
for i in range(1, num + 1):
    s += "".join(str(i) * i)
    if len(s) >= num:
        break


print(s[:num])
