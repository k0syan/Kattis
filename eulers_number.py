def el(x):
    if x == 1 or x == 0:
        return 1
    else:
        return int(x * el(x - 1))


n = int(input())
total = 1
for i in range(1, n + 1):
    total += (1 / el(i))
print(total)
