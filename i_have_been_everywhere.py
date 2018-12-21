n = int(input())
while n != 0:
    c = int(input())
    cities = []
    while c != 0:
        city = input()
        if city not in cities:
            cities.append(city)
        c -= 1
    print(len(cities))
    n -= 1
