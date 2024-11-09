def solve():
    n = int(input())
    blood = list(map(int, input().split()))
    ans = 0

    def dfs(h):
        nonlocal ans
        if is_die():
            ans += 1
            return
        if h == 0:
            return

        for i in range(n):
            if blood[i] > 0:
                blood[i] -= h
                dfs(h - 1)
                blood[i] += h

    def is_die():
        for i in range(n):
            if blood[i] > 0:
                return False
        return True

    if n >= 6:
        print(0)
        return

    dfs(5)
    print(ans)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
