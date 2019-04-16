if __name__ == "__main__":
    while True:
        a, b = [int(i) for i in input().split()]
        if a == 0 and b == 0:
            break
        if a + b == 13:
            print("Never speak again.")
        elif a == b:
            print("Undecided.")
        elif a > b:
            print("To the convention.")
        elif a < b:
            print("Left beehind.")
