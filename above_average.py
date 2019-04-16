if __name__ == "__main__":
    n = int(input())
    while n != 0:
        tmp = [int(i) for i in input().split()]
        avg = sum(tmp[1:]) / tmp[0]
        total = 0
        for grade in tmp[1:]:
            if grade > avg:
                total += 1
        print("{:.3f}%".format(total / tmp[0] * 100))
        n -= 1
