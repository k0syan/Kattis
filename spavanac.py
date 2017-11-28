""" Created by Shahen Kosyan on 11/28/17 """

if __name__ == "__main__":
    h, m = [int(x) for x in input().split()]
    ah, am = 0, 0
    if m >= 45:
        ah = h
        am = m - 45
    else:
        ah = h - 1
        am = m + 15

    if ah == -1:
        ah = 23

    print(ah, am)
