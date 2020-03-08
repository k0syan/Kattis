n, h, v = [int(x) for x in input().split()]

ht = h
vt = v
if h < n / 2:
    ht = n - h
if v < n / 2:
    vt = n - v

print(vt * ht * 4)
