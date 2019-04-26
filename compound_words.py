import sys

if __name__ == "__main__":
    words = []
    final_list = []
    for line in sys.stdin:
        line = line.strip().split()
        for l in line:
            words.append(l)
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            final_list.append(words[i] + words[j])
            final_list.append(words[j] + words[i])

    final_list.sort()
    final = []
    for w in final_list:
        if w not in final:
            final.append(w)

    for w in final:
        print(w)
