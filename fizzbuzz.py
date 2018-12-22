tmp = input().split()
x, y, n = int(tmp[0]), int(tmp[1]), int(tmp[2])
for i in range(1, n + 1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0:
        print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)
