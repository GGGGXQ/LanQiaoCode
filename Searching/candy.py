ans = 0


def dfs(deep, n, m):
    global ans
    if deep == 7:
        if n == 0 and m == 0:
            ans += 1
        return
    for i in range(n + 1):
        for j in range(m + 1):
            if 2 <= i + j <= 5:
                dfs(deep + 1, n - i, m - j)


if __name__ == '__main__':
    dfs(0, 9, 16)
    print(ans)
