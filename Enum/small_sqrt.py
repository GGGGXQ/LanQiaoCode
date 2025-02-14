if __name__ == '__main__':
    n = int(input())

    res = 0
    for i in range(1, n):
        if i ** 2 % n < n / 2:
            res += 1
    print(res)