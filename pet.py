points = 0
ind = 0

for i in range(5):
    tmp = input().split()
    point = int(tmp[0]) + int(tmp[1]) + int(tmp[2]) + int(tmp[3])
    if points < point:
        points = point
        ind = i + 1

print(ind, points)
