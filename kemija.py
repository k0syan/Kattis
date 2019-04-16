if __name__ == "__main__":
    vowels = ["a", "e", "i", "o", "u"]
    words = input().split()
    answer = []
    for word in words:
        finalWord = []
        lettersList = list(word)
        i = 0
        while i < len(lettersList):
            letter = lettersList[i]
            finalWord.append(letter)
            if letter in vowels:
                i += 3
            else:
                i += 1
        answer.append("".join(finalWord))
    print(" ".join(answer))
