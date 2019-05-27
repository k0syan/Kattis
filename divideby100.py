if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a = n / m
    b = str(a).rstrip("0")
    x = b.split(".")
    answer = x[0]
    y = x[1]
    if y != "":
        answer += "." + y

    print(answer)
