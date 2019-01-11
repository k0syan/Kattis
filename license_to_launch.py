if __name__ == "__main__":
    n = int(input())
    tmp = [int(i) for i in input().split()]
    a = min(tmp)
    print(tmp.index(a))
