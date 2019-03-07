if __name__ == "__main__":
    sentence = input().split()
    totalCount = 0
    for word in sentence:
        if word.count("ae") != 0:
            totalCount += 1

    if totalCount / len(sentence) * 100 >= 40:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")
