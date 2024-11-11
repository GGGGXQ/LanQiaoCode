def dfs(cx, cy, count):
    global ans
    if count == 16:
        ans += 1
        return ans

    for x, y in directions:
        nx, ny = x + cx, y + cy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, count + 1)
                visited[nx][ny] = 0


if __name__ == '__main__':
    ans = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            visited[i][j] = 1
            dfs(i, j, 1)
            visited[i][j] = 0
    print(ans)
