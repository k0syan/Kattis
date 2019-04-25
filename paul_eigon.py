if __name__ == "__main__":
    n, p, q = [int(i) for i in input().split()]
    if int(((p + q) / n)) % 2 == 0:
        print("paul")
    else:
        print("opponent")
