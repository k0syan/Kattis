def fib(number):
    current = 1
    old = 0
    i = 1
    while i < number:
        current, old, i = current + old, current, i + 1
    return current


if __name__ == "__main__":
    n = int(input())
    if n == 1:
        print(0, 1)
    else:
        print(fib(n - 1), fib(n))
