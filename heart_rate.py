n = int(input())
for i in range(n):
    b, p = [float(x) for x in input().split()]
    bpm = 60 * b / p
    miBpm = bpm - 60 / p
    maBpm = bpm + 60 / p
    print(format(miBpm, '.4f'), format(bpm, '.4f'), format(maBpm, '.4f'))