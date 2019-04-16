def solution(rules):
    finalLetters = []
    final = []
    a, b = rules[0].split(">")
    a = list(a)[1]
    b = list(b)[0]
    finalLetters.append(a)
    finalLetters.append(b)
    for i in range(1, len(rules)):
        a, b = rules[i].split(">")
        a = list(a)[1]
        b = list(b)[0]
        print(finalLetters)
        if a in finalLetters and b in finalLetters:
            if finalLetters.index(a) > finalLetters.index(b):
                print(a, b)

        elif a in finalLetters:
            if b not in finalLetters:
                finalLetters.insert(finalLetters.index(a) + 1, b)
        elif b in finalLetters:
            if a not in finalLetters:
                if finalLetters.index(b) == 0:
                    finalLetters.insert(1, b)
                    finalLetters[0] = a
                else:
                    finalLetters.insert(finalLetters.index(b), a)
        else:
            finalLetters.append(a)
            finalLetters.append(b)

    return "".join(finalLetters)


inp = input().split(", ")
print(solution(inp))

# switzerland

# “U>N”, “R>Y”, “H>U”, “N>G”, “A>R”, “G>A”
# "P>E", "R>U", "E>R"
# "R>U", "P>E", "E>R"
