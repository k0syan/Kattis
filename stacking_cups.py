if __name__ == "__main__":
    n = int(input())
    colors = []
    radiuses = []
    diameters = []
    while n != 0:
        tmp = input().split()
        if tmp[0].isnumeric():
            radius = int(int(tmp[0]) / 2)
            color = tmp[1]
            radiuses.append(radius)
            colors.append(color)
        else:
            radius = int(tmp[1])
            color = tmp[0]
            radiuses.append(radius)
            colors.append(color)
        n -= 1

    orderdRadiuses = radiuses.copy()
    orderdRadiuses.sort()
    for r in orderdRadiuses:
        print(colors[radiuses.index(r)])

