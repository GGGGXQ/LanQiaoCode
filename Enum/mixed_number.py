if __name__ == '__main__':
    n = int(input())
    res = 0
    for a in range(1, n):
        M = 1
        b = (n - a) * M
        c = M

        s = str(b) + str(c) + str(a)
        while len(s) <= 9:
            M += 1
            st = set(s)
            if len(s) == 9 and len(st) == 9 and '0' not in st:
                res += 1

            b = (n - a) * M
            c = M
            s = str(b) + str(c) + str(a)
    print(res)