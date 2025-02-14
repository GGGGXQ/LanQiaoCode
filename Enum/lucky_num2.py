if __name__ == '__main__':
    ans = 0
    for i in range(1, 100000001):
        s = str(i)
        n = len(s)
        if n % 2 != 0:
            continue

        l, r = 0, 0
        for j in range(n):
            if j < n // 2:
                l += int(s[j])
            else:
                r += int(s[j])
        if l == r:
            ans += 1
    print(ans)