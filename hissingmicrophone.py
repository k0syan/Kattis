""" Created by Shahen Kosyan on 11/28/17 """

if __name__ == "__main__":
    s = input()
    n = 0
    hissing = False
    sl = False
    while n < len(s):
        if s[n] == "s":
            if sl:
                hissing = True
                break
            sl = True
        else:
            sl = False
        n += 1

    if hissing:
        print("hiss")
    else:
        print("no hiss")