if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if len(line) == 0:
            break
        else:
            lines.append(line)
    sentence = " ".join(lines).split()
    existing = []
    answer = []
    for word in sentence:
        if word.lower() in existing:
            answer.append(".")
        else:
            existing.append(word.lower())
            answer.append(word)
    print(" ".join(answer))
