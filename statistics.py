import sys

c = 1
for line in sys.stdin:
    if len(line) == 0:
        break
    line = [int(i) for i in line.split()]
    count = line[0]
    numbers = line[1:]
    numbers.sort()
    minimum = numbers[0]
    maximum = numbers[count - 1]

    print("Case {}: {} {} {}".format(c, minimum, maximum, maximum - minimum))
    c += 1
