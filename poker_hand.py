strings = input().split()
letters = list("A23456789TJQK")
powers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(5):
    letter = list(strings[i])[0]
    ind = letters.index(letter)
    powers[ind] += 1

print(max(powers))
