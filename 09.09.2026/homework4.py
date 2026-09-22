"""Задача Код"""

nums = []
approved_numbers = []
matrix = [
            [[0], [3], [1], [7], [5], [9], [8], [6], [4], [2]],
            [[7], [0], [9], [2], [1], [5], [4], [8], [6], [3]],
            [[4], [2], [0], [6], [8], [7], [1], [3], [5], [9]],
            [[1], [7], [5], [0], [9], [8], [3], [4], [2], [6]],
            [[6], [1], [2], [3], [0], [4], [5], [9], [7], [8]],
            [[3], [6], [7], [4], [2], [0], [9], [5], [8], [1]],
            [[5], [8], [6], [9], [7], [2], [0], [1], [3], [4]],
            [[8], [9], [4], [5], [3], [6], [2], [0], [1], [7]],
            [[9], [4], [3], [8], [6], [1], [7], [2], [0], [5]],
            [[2], [5], [8], [1], [4], [3], [6], [7], [9], [0]],
]

while True:
    try:
        num = input().strip()
        nums.append(num)
    except EOFError:
        break

def find_k(num: str) -> int:
    k = 0
    for s in range(len(num)):
        d = int(num[s])
        k = matrix[k][d][0]
    return k

for i in range(len(nums)):
    f = 0
    s = 1
    num = nums[i]
    k = find_k(num)
    original_list = list(num)
    while k != 0:
        reverse_list = original_list.copy()
        if 0 <= f < len(num) and 0 < s < len(num):
            reverse_list[f], reverse_list[s] = original_list[s], original_list[f]
        else:
           raise ValueError(f"Число {num} не имеет решения")
        reversed_num = "".join(reverse_list)
        k = find_k(reversed_num)
        num = reversed_num
        f+=1
        s+=1
    approved_numbers.append(num)


with open("output.dat", "w") as file:
    file.write("\n".join(approved_numbers))
