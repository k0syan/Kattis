def read_data():
    with open("text.txt") as fp:
        for line in fp:
            features = [float(x) for x in line.split()]
            print(features)


def get_change(a, p):
    t = a * 100
    p = p * 100
    diff = t - p
    arr = [0, 0, 0, 0, 0, 0]

    while diff != 0:
        if diff >= 100:
            diff -= 100
            arr[5] += 1
        elif diff >= 50:
            diff -= 50
            arr[4] += 1
        elif diff >= 25:
            diff -= 25
            arr[3] += 1
        elif diff >= 10:
            diff -= 10
            arr[2] += 1
        elif diff >= 5:
            diff -= 5
            arr[1] += 1
        else:
            diff -= 1
            arr[0] += 1

    return arr


if __name__ == "__main__":
    print(get_change(5, 0.99))
