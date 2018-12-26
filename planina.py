import math
number = int(input())


def solve(n):
    if n == 1:
        return 9
    return int((math.sqrt(solve(n - 1)) * 2 - 1) ** 2)


print(solve(number))
