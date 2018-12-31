if __name__ == "__main__":
    n = int(input())
    b = list("{0:b}".format(n))
    b.reverse()
    r = "".join(b)
    print(int(r, 2))
