if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    for k in range(min(a, b) + 1, max(a, b) + 2):
        print(k)
