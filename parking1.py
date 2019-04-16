if __name__ == "__main__":
    a, b, c = [int(i) for i in input().split()]
    print(a, b, c)
    total = 0
    fs, fe = [int(i) for i in input().split()]
    ss, se = [int(i) for i in input().split()]
    ts, te = [int(i) for i in input().split()]

    starts = [fs, ss, ts]
    ends = [fe, se, te]
    starts.sort()
    ends.sort()

