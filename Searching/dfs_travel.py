def dfs(start, way, step):
    global ways
    if step == 20:
        if m in way:
            way.append(m)
            ways.append(list(map(str, way)))
        return

    for j in cities_link[start]:
        if visited[j - 1] == 0:
            visited[j - 1] = 1
            way.append(j)
            dfs(j, way.copy(), step + 1)
            way.pop()
            visited[j - 1] = 0


if __name__ == '__main__':
    cities_link = [0]
    for _ in range(1, 21):
        r, p, k = list(map(int, input().split()))
        cities_link.append((r, p, k))
    m = int(input())
    ways = []
    visited = [0] * 20
    dfs(m, [m], 1)
    visited[m - 1] = 1
    for i in range(1, len(ways) + 1):
        print(f"{i}: {' '.join(ways[i - 1])}")
