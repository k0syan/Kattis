""" Created by Shahen Kosyan on 11/28/17 """

if __name__ == "__main__":
    n, w, l = [int(x) for x in input().split()]
    answer = ""
    while n > 0:
        n -= 1
        tmp = int(input())
        if tmp <= w or tmp <= l or tmp * tmp <= w * w + l * l:
            answer += "DA\n"
        else:
            answer += "NE\n"

    print(answer[:-1])