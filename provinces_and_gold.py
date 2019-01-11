if __name__ == "__main__":
    tmp = input().split()
    g, s, c = int(tmp[0]), int(tmp[1]), int(tmp[2])
    total = g * 3 + s * 2 + c * 1
    if total >= 8:
        print("Province or Gold")
    elif total >= 6:
        print("Duchy or Gold")
    elif total >= 5:
        print("Duchy or Silver")
    elif total >= 3:
        print("Estate or Silver")
    elif total >= 2:
        print("Estate or Copper")
    else:
        print("Copper")
