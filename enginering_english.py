import sys

existing = []
for line in sys.stdin:
    line = line.strip()
    sentence = line.split(" ")
    answer = []
    for word in sentence:
        if word.lower() in existing:
            answer.append(".")
        else:
            existing.append(word.lower())
            answer.append(word)
    print(" ".join(answer))
