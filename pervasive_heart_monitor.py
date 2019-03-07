import sys

for line in sys.stdin:
    if len(line) == 0:
        break
    arr = line.split()
    name = ""
    rates = []
    for a in arr:
        r = -5.0
        try:
            r = float(a)
        except ValueError:
            r = -5.0

        if r != -5.0:
            rates.append(r)
        else:
            name = name + a + " "

    print(str("%.6f" % (sum(rates) / len(rates))) + " " + name)
