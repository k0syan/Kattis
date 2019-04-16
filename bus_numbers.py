if __name__ == "__main__":
    n = int(input())
    buses = [int(i) for i in input().split()]
    buses.sort()
    answer = []
    prev = 0
    count = 0
    for i in range(len(buses)):
        cur = buses[i]
        if cur - prev == 1:
            count += 1
        else:
            answer.append(cur)

        if count > 2:

    print(answer)
