if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        task = input()
        if task == "P=NP":
            print("skipped")
        else:
            tmp = list(task)
            a, b = int(tmp[0]), int(tmp[len(tmp) - 1])
            print(a + b)
