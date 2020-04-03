n = int(input())
ints = [int(x) for x in input().split()]
a = 0
b = 0
i = 0
ints.sort()
ints.reverse()
for i in range(n):
    if i % 2 == 0:
        a += ints[i]
    else:
        b += ints[i]
print(a, b)
