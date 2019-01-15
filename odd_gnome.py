if __name__ == "__main__":
    n = int(input())
    while n != 0:
        tmp = [int(i) for i in input().split()]

        for i in range(2, len(tmp)):
            v0 = tmp[i - 1]
            v1 = tmp[i]
            v2 = tmp[i + 1]

            if v0 > v1:
                if v2 > v0:
                    print(i)
                    break
                if v0 > v2 > v1:
                    print(i - 1)
                    break
            elif v1 > v2 > v0:
                print(i)
                break

        n -= 1

# 1
# 7 1 2 3 4 8 5 6
# 5 3 4 5 2 6
# 4 10 20 11 12