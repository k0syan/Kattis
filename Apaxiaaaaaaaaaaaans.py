name = list(input())
finalName = [name[0]]
for i in range(1, len(name)):
    if finalName[len(finalName) - 1] != name[i]:
        finalName.append(name[i])

print("".join(finalName))
