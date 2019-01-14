if __name__ == "__main__":
    tmp = input().split()
    r, n = int(tmp[0]), int(tmp[1])
    rooms = []
    while n != 0:
        room = int(input())
        rooms.append(room)
        n -= 1

    if len(rooms) == r:
        print("too late")
    else:
        for i in range(1, r + 1):
            if i not in rooms:
                print(i)
                break
