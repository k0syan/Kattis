import math

t = int(input())
while t != 0:
    needed = int(input())
    print(math.ceil(needed / 400))
    t -= 1
