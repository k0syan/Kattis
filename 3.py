def read_data():
    with open("text.txt") as fp:
        for line in fp:
            features = [float(x) for x in line.split()]
            print(features)

# domino

def domino(d):
    a = str(d).split(",")
    b = []
    for a1 in a:
        b.append(a1.split("-"))
    length = 1
    lengths = []
    for i in range(len(b) - 1):
        bc = b[i]
        bn = b[i + 1]
        if bc[1] == bn[0]:
            length += 1
        else:
            lengths.append(length)
            length = 1

        if i == len(b) - 2:
            lengths.append(length)
    return max(lengths)


if __name__ == "__main__":
    print(domino("1-2,2-2,3-3,3-4,4-5,1-1,1-2"))




# "1-1"
# "1-2,1-2"
# "3-2,2-1,1-4,4-4,5-4,4-2,2-1"
# "5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5"
# "1-1,3-5,5-5,5-4,4-2,1-3"
# "1-2,2-2,3-3,3-4,4-5,1-1,1-2"