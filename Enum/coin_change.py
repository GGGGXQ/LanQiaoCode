if __name__ == '__main__':
    a = [0] * 100000
    ans = 0
    for i in range(1, 2024):
        a[i] = i

    for i in range(2, 4047):
        res = 0
        for j in range(2, i // 2 + 1):
            k = i - j
            if j != k:
                res += min(a[j], a[k])
            else:
                res += a[j] // 2
        res += a[i]
        ans = max(res, ans)
    print(ans)