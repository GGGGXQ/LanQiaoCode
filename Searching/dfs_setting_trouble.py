def solve():
    n = int(input())
    r_map = [list(input().strip()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    s = [(0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if dfs(s, n, r_map, visited, directions):
        if dfs(s, n, r_map, visited, directions):
            print(2)
        else:
            print(1)
    else:
        print(0)


def dfs(s, n, r_map, visited, directions):
    ans = 0
    while s:
        cx, cy = s.pop()
        for x, y in directions:
            nx, ny = x + cx, y + cy
            if n > nx >= 0 and 0 <= ny < n:
                if visited[nx][ny] == 1 or r_map[nx][ny] == 'X':
                    continue
                if nx == ny == n - 1:
                    ans += 1
                    return ans
                visited[nx][ny] = 1
                s.append((nx, ny))
    return ans


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
