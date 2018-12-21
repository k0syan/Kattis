n = int(input())
group = input().split()
final = []
for i in range(n):
    tmp = group[i]
    if group.count(tmp) == 1:
        final.append(tmp)
if len(final) != 0:
    m = max(final)
    print(group.index(str(m)) + 1)
else:
    print("none")
