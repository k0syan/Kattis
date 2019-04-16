if __name__ == "__main__":
    n = int(input())
    days = [int(i) for i in input().split()]
    days.sort()
    arr = []
    for i in range(n):
        arr.append(2 + i + days[len(days) - 1 - i])
    print(max(arr))
