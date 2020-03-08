n = int(input())
wu = []
while n != 0:
    u, t = input().split()
    if u not in wu and len(wu) != 12:
        wu.append(u)
        print(u + " " + t)
    n -= 1

