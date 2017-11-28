""" Created by Shahen Kosyan on 11/28/17 """

if __name__ == "__main__":
    cards = input()
    tc = 0
    cc = 0
    gc = 0
    n = 0
    while n < len(cards):
        if cards[n] == "T":
            tc += 1
        elif cards[n] == "C":
            cc += 1
        else:
            gc += 1
        n += 1

    mc = tc
    if mc > gc:
        mc = gc

    if mc > cc:
        mc = cc

    print(tc * tc + cc * cc + gc * gc + mc * 7)