import math

if __name__ == "__main__":
    c = int(input())

    needed = math.ceil(c / 2)
    days = 1
    while needed != 0:
        days += 1
        needed = math.ceil(needed / 2)
        if needed == 1:
            days += 1
            break
    if c == 1:
        print(c)
    elif c == 2:
        print(c)
    else:
        print(days)
    # if c == 1:
    #     print(1)
    # elif c % 2 == 1:
    #     print(int(c / 2) + 2)
    # else:
    #     print(int(c / 2) + 1)
