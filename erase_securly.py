if __name__ == "__main__":
    n = int(input())
    x = n % 2
    a = [int(i) for i in list(input())]
    b = [int(i) for i in list(input())]

    succeed = True
    if x == 1:
        for i in range(len(a)):
            if a[i] == b[i]:
                succeed = False
                break
        if succeed:
            print("Deletion succeeded")
        else:
            print("Deletion failed")
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                succeed = False
                break
        if succeed:
            print("Deletion succeeded")
        else:
            print("Deletion failed")
