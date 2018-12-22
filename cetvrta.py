first = input().split()
x0, y0 = int(first[0]), int(first[1])
second = input().split()
x1, y1 = int(second[0]), int(second[1])
third = input().split()
x2, y2 = int(third[0]), int(third[1])
x = [x0, x1, x2]
y = [y0, y1, y2]

y4, x4 = 0, 0
if x.count(x0) % 2 == 1:
    x4 = x0
elif x.count(x1) % 2 == 1:
    x4 = x1
elif x.count(x2) % 2 == 1:
    x4 = x2

if y.count(y0) % 2 == 1:
    y4 = y0
elif y.count(y1) % 2 == 1:
    y4 = y1
elif y.count(y2) % 2 == 1:
    y4 = y2

print(x4, y4)
