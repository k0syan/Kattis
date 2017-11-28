""" Created by Shahen Kosyan on 11/28/17 """

if __name__ == "__main__":
    autors = input().split("-")
    answer = ""
    n = 0
    while n < len(autors):
        answer += autors[n][0]
        n += 1

    print(answer)