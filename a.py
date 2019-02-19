def read_data():
    array = []
    with open("text.txt") as fp:
        for line in fp:
            features = [float(x) for x in line.split()]
            if len(features) == 1:
                array.append(features[0])
            else:
                array.append(features)
        return array


def numberOfCarryOperations(a, b):
    al = [int(i) for i in list(str(a))]
    bl = [int(i) for i in list(str(b))]

    if len(al) > len(bl):
        while len(al) != len(bl):
            bl.insert(0, 0)
    elif len(bl) > len(al):
        while len(al) != len(bl):
            al.insert(0, 0)

    c = 0

    bl.insert(0, 0)
    al.insert(0, 0)

    for i in range(len(al)):
        a1 = al[len(al) - i - 1]
        b1 = bl[len(bl) - i - 1]

        if a1 + b1 >= 10:
            c += 1
            j = len(al) - i - 2
            while j != 0:
                if al[j] == 9:
                    al[j] = 0
                    c += 1
                else:
                    al[j] += 1
                    break
                j -= 1

    return c


if __name__ == "__main__":
    print(numberOfCarryOperations(123, 456))
    print(numberOfCarryOperations(555, 555))
    print(numberOfCarryOperations(900, 11))
    print(numberOfCarryOperations(145, 55))
    print(numberOfCarryOperations(0, 0))
    print(numberOfCarryOperations(1, 99999))
    print(numberOfCarryOperations(999045, 1055))
    print(numberOfCarryOperations(101, 809))
    print(numberOfCarryOperations(189, 209))

    # numberOfCarryOperations(123, 456) // 0
    # numberOfCarryOperations(555, 555) // 3
    # numberOfCarryOperations(900, 11) // 0
    # numberOfCarryOperations(145, 55) // 2
    # numberOfCarryOperations(0, 0) // 0
    # numberOfCarryOperations(1, 99999) // 5
    # numberOfCarryOperations(999045, 1055) // 5
    # numberOfCarryOperations(101, 809) // 1
    # numberOfCarryOperations(189, 209) // 1