if __name__ == "__main__":
    n = int(input())
    total = 0
    expenses = [int(i) for i in input().split()]
    for e in expenses:
        if e < 0:
            total -= e
    print(total)
