t = int(input())
while t != 0:
    a = input().split()
    if len(a) > 1 and a[0] == "Simon" and a[1] == "says":
        print(" ".join(a[2:]))
    else:
        print()
    t -= 1
