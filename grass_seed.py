cost = float(input())
count = int(input())
totalCost = 0
while count > 0:
    tmp = input().split()
    width, length = float(tmp[0]), float(tmp[1])
    area = width * length
    totalCost += area * cost
    count -= 1

print(totalCost)
