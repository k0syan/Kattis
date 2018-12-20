def sumofdigits(number):
    total = 0
    while number != 0:
        total += int(number % 10)
        number = int(number / 10)

    return total


l = int(input())
d = int(input())
x = int(input())

minimum = 0
maximum = 0

for i in range(l, d + 1):
    if sumofdigits(i) == x:
        if minimum == 0:
            minimum = i

    if sumofdigits(i) == x and i > maximum:
        maximum = i

print(minimum)
print(maximum)

