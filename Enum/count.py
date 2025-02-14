if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    r = [0] * (m + 1)
    l = [0] * (m + 1)

    for i in arr:
        if 0 < i <= m:
            r[i] += 1
        elif i < 0 and abs(i) <= m:
            l[abs(i)] += 1

    for i in range(1, m + 1):
        r[i] += r[i - 1]
        l[i] += l[i - 1]

    ans = 0
    for j in range(1, m // 2 + 1):
        ans = max(ans, r[j] + l[m - 2 * j], l[j] + r[m - 2 * j])

    ans = max(r[m], l[m], ans)
    if 0 in arr:
        ans += 1

    print(ans)