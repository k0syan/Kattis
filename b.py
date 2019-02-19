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


def numberOfFriends(r, req):
    rs = []
    for r1 in r:
        rs.append(r1.split(":"))
    results = []
    for i in range(len(rs)):
        current = rs[i][0]
        results.append([current, 1])
        n = rs[i][1]
        c = current
        for j in range(i + 1, len(rs)):
            if n == rs[j][0]:
                for res in results:
                    if res[0] == current:
                        res[1] += 1
                        break
                c = n
                n = rs[j][1]

    returnResult = ""
    print(req)
    for i in range(len(req)):
        rn = req[i]
        for rr in results:
            if rr[0] == rn:
                returnResult += rn + ":" + str(rr[1])
        if i != len(req) - 1:
            returnResult += ", "

    return returnResult


if __name__ == "__main__":
    print(numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"]))
