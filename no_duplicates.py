array = input().split()
finalArray = [array[0]]
noDuplicates = "YES"
for i in range(1, len(array)):
    if array[i] in finalArray:
        noDuplicates = "NO"
        break
    else:
        finalArray.append(array[i])

print(noDuplicates)
