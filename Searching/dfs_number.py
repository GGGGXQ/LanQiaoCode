import sys


def dfs(x, y, vec):
    global n, k, a, visited, line, directions
    if x == n and y == n:
        if len(vec) != n * n - 1:
            return
        print(''.join(map(str, vec)))
        sys.exit(0)

    for i in range(8):
        tx = x + directions[i][0]
        ty = y + directions[i][1]
        if not (1 <= tx <= n and 1 <= ty <= n and visited[tx][ty] == 0):
            continue
        if (a[x][y] + 1) % k != a[tx][ty]:
            continue
        if i == 1 and (line[x - 1][y][x][y + 1] == 1 or line[x][y + 1][x - 1][y] == 1):
            continue
        if i == 3 and (line[x + 1][y][x][y + 1] == 1 or line[x][y + 1][x + 1][y] == 1):
            continue
        if i == 5 and (line[x][y - 1][x + 1][y] == 1 or line[x + 1][y][x][y - 1] == 1):
            continue
        if i == 7 and (line[x][y - 1][x - 1][y] == 1 or line[x - 1][y][x][y - 1] == 1):
            continue

        vec.append(i)
        if abs(directions[i][0]) + abs(directions[i][1]) == 2:
            line[x][y][tx][ty] = 1
        visited[tx][ty] = 1
        dfs(tx, ty, vec)
        vec.pop()
        if abs(directions[i][0]) + abs(directions[i][1]) == 2:
            line[x][y][tx][ty] = 0
        visited[tx][ty] = 0


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    line = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            a[i][j] = row[j - 1]

    visited[1][1] = 1
    vec = []
    dfs(1, 1, vec)
    print(-1)
