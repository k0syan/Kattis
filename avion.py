ans = []
i = 1
while i < 6:
    inp = input()
    if "FBI" in inp:
        ans.append(str(i))
    i += 1
if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(ans))
