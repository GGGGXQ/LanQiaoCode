import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)  # 设置递归层数防止越栈

ans = 0


def solve():
    n, m = map(int, input().split())
    h_map = [list(input()) for i in range(n)]
    directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if h_map[i][j] == 'S':
                visited[i][j] = 1
                dfs(n, m, i, j, h_map, directions, visited)
                break


def dfs(n, m, cx, cy, h_map, directions, visited):
    global ans
    if cx < 0 or cy < 0 or cx >= n or cy >= m:
        return

    for x, y in directions:
        cx_to_tx, cy_to_ty = x + cx, y + cy
        if 0 <= cx_to_tx < n and 0 <= cy_to_ty < m and visited[cx_to_tx][cy_to_ty] == 0:
            if h_map[cx_to_tx][cy_to_ty] == 'x':
                continue
            if h_map[cx_to_tx][cy_to_ty] == 'b':
                ans += 1
                visited[cx_to_tx][cy_to_ty] = 1
                dfs(n, m, cx_to_tx, cy_to_ty, h_map, directions, visited)
            else:
                visited[cx_to_tx][cy_to_ty] = 1
                dfs(n, m, cx_to_tx, cy_to_ty, h_map, directions, visited)
    return ans


if __name__ == '__main__':
    solve()
    print(ans)
