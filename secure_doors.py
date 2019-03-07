if __name__ == "__main__":
    n = int(input())
    entered = []
    while n != 0:
        a, b = input().split()
        if a == "entry":
            if b in entered:
                print(b + " entered " + "(ANOMALY)")
            else:
                print(b + " entered ")
                entered.append(b)
        else:
            if b in entered:
                print(b + " exited")
                entered.remove(b)
            else:
                print(b + " exited (ANOMALY)")
        n -= 1
