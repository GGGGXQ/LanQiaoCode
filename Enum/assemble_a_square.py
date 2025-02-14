if __name__ == '__main__':
    S = 7385137888721 * 4 + 10470245
    a = 1000000
    while a * a < S:
        a += 1
    print(a - 1)