n = int(input())
answers = list(input())

ads, brs, gos = 0, 0, 0
for i in range(n):
    a = answers[i]
    if a == "A":
        if i % 3 == 0:
            ads += 1
        if i % 4 == 1:
            brs += 1
        if i % 6 == 2 or i % 6 == 3:
            gos += 1
    elif a == "B":
        if i % 3 == 1:
            ads += 1
        if i % 2 == 0:
            brs += 1
        if i % 6 == 4 or i % 6 == 5:
            gos += 1
    else:
        if i % 3 == 2:
            ads += 1
        if i % 4 == 3:
            brs += 1
        if i % 6 == 0 or i % 6 == 1:
            gos += 1

m = max(ads, brs, gos)
print(m)
if ads == m:
    print("Adrian")
if brs == m:
    print("Bruno")
if gos == m:
    print("Goran")
