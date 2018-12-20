def sumfrombase(b, nn):
    total = 0
    while nn != 0:
        t = int(nn % b)
        total += t * t
        nn = int(nn / b)
    return total


n = int(input())

while n != 0:
    tmp = input().split()
    s, base, number = int(tmp[0]), int(tmp[1]), int(tmp[2])
    print(s, sumfrombase(base, number))
    n -= 1
