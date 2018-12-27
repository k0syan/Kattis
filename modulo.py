n = 10
array = []
while n != 0:
    a = int(input())
    r = a % 42
    if r not in array:
        array.append(r)
    n -= 1

print(len(array))
