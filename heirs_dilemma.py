def correct(x):
    digits = [int(k) for k in list(str(x))]
    existingDigits = []
    for digit in digits:
        if digit in existingDigits:
            return False
        else:
            if digit == 0:
                return False
            if x % digit == 0:
                existingDigits.append(digit)
            else:
                return False
    return True


if __name__ == "__main__":
    a, b = [int(i) for i in input().split()]
    total = 0
    for i in range(a, b + 1):
        if correct(i):
            total += 1
    print(total)
