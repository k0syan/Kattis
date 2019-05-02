if __name__ == "__main__":
    m, n = [int(i) for i in input().split()]
    salaries = {}
    while m != 0:
        a, b = input().split()
        salaries[a] = b
        m -= 1
    while n != 0:
        total = 0
        new = False
        while True:
            text = input().split()
            for t in text:
                if t == ".":
                    n -= 1
                    new = True
                    break
                else:
                    s = salaries.get(t, 0)
                    total += int(s)
            if new:
                new = False
                break
        print(total)
