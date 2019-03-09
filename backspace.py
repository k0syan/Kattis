if __name__ == "__main__":
    answer = []
    letters = list(input())
    for l in letters:
        if l == "<":
            answer.pop()
        else:
            answer.append(l)
    print("".join(answer))
