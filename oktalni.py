binary = [int(x) for x in list(input())]
while len(binary) % 3 != 0:
    binary.insert(0, 0)
ans = []
for i in range(0, len(binary), 3):
    ta = 0
    for j in range(i, i + 3):
        # print("ta = ", ta, " j = ", j)
        k = binary[j] * int(pow(2, 2 - j % 3))
        # print(binary[j])
        # print("k = ", k)
        # print("K = ", k)
        ta += k
    ans.append(ta)
    # print("ans = ", ans)
print(int("".join(str(x) for x in ans)))