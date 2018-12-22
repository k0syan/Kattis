n = int(input())
total = []
while n != 0:
    tmp = input().split()
    start, end = int(tmp[0]), int(tmp[1])
    arr = list(range(start, end + 1))
    total += arr
    n -= 1
total = list(set(total))
print(len(total))
