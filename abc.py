numbers = [int(n) for n in input().split()]
numbers.sort()
letters = list(input())
final = [0, 0, 0]

for i in range(len(letters)):
    if letters[i] == "A":
        final[i] = int(numbers[0])
    elif letters[i] == "B":
        final[i] = int(numbers[1])
    else:
        final[i] = int(numbers[2])

print(final[0], final[1], final[2])
