from collections import Counter, defaultdict


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split())))
    ans = 0

    right = defaultdict(Counter)
    left = defaultdict(Counter)
    for i in range(n):
        for j in range(m):
            x = g[i][j]
            ans += right[i + j][x] + left[j - i][x]
            right[i + j][x] += 1
            left[j - i][x] += 1
    print(ans * 2)