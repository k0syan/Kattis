t = int(input())
while t != 0:
    string = input().split()
    if len(string) > 1 and string[0] == "simon" and string[1] == "says":
        print(" ".join(string[2:]))
    else:
        print()
    t -= 1
