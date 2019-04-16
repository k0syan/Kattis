import sys

if __name__ == "__main__":
    dictionary = []
    for line in sys.stdin:
        print(line)
        if len(line) == 0:
            break
        dictionary.append(line.split())

    # print(dictionary)
