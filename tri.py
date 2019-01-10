if __name__ == "__main__":
    tmp = input().split()
    x, y, z = int(tmp[0]), int(tmp[1]), int(tmp[2])
    if x == y / z:
        s = str(x) + "=" + str(y) + "/" + str(z)
        print(s)
    elif x == y * z:
        s = str(x) + "=" + str(y) + "*" + str(z)
        print(s)
    elif x == y + z:
        s = str(x) + "=" + str(y) + "+" + str(z)
        print(s)
    elif x == y - z:
        s = str(x) + "=" + str(y) + "-" + str(z)
        print(s)
    elif x * y == z:
        s = str(x) + "*" + str(y) + "=" + str(z)
        print(s)
    elif x / y == z:
        s = str(x) + "/" + str(y) + "=" + str(z)
        print(s)
    elif x + y == z:
        s = str(x) + "+" + str(y) + "=" + str(z)
        print(s)
    elif x - y == z:
        s = str(x) + "-" + str(y) + "=" + str(z)
        print(s)
