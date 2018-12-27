while 1 == 1:
    t = int(input())
    if t == -1:
        break
    totalDistance = 0
    prevTime = 0
    while t != 0:
        tmp = input().split()
        s, time = int(tmp[0]), int(tmp[1])
        totalDistance += s * (time - prevTime)
        prevTime = time
        t -= 1
    print(totalDistance, "miles")
