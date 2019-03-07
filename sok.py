if __name__ == "__main__":
    sok = [int(i) for i in input().split()]
    ratio = [int(r) for r in input().split()]

    count = 999
    for i in range(len(sok)):
        if count > sok[i] / ratio[i]:
            count = sok[i] / ratio[i]

    aleft = sok[0] - ratio[0] * count
    bleft = sok[1] - ratio[1] * count
    cleft = sok[2] - ratio[2] * count

    print("%.6f" % aleft, "%.6f" % bleft, "%.6f" % cleft)
