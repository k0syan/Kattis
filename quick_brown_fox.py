if __name__ == "__main__":
    n = int(input())
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    while n != 0:
        missing = []
        sentence = [i.lower() for i in list(input())]
        for letter in alphabet:
            if letter not in sentence:
                missing.append(letter)
        if len(missing) == 0:
            print("pangram")
        else:
            print("missing " + "".join(missing))
        n -= 1
