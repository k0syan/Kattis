if __name__ == "__main__":
    score = 0
    total = 0
    tries = []
    success = []
    while True:
        data = input()
        if data == "-1":
            break
        else:
            data = data.split()
            time = int(data[0])
            task = data[1]
            result = data[2]
            if result == "wrong":
                tries.append(task)
            else:
                total += 1
                score += time
                score += 20 * tries.count(task)
    print(total, score)
