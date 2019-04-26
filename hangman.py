if __name__ == "__main__":
    word = list(input())
    letters = list(input())

    incorrect = 0
    for letter in letters:
        if letter not in word:
            incorrect += 1
        else:
            while letter in word:
                word.remove(letter)

        if len(word) == 0:
            break
        if incorrect == 10:
            break

    if incorrect < 10:
        print("WIN")
    else:
        print("LOSE")
