class Edge:
    def __init__(self, x, y, l, id):
        self.x = x
        self.y = y
        self.l = l
        self.id = id

if __name__ == '__main__':
    n = int(input())
    e = [None] * (n + 10)
    connect = [[] for _ in range(n + 1)]

    for i in range(1, n):
        x , y = map(int,input().split())
        e[i] = Edge(x ,i + 1, y, i)
        connect[x].append(e[i])
        connect[i + 1].append(e[i])

    for i in range(1, n + 1):
        connect[i].sort(key=lambda x: x.l, reverse=True)

    ans = 0
    for i in range(1, n + 1):
        if len(connect[i]) >= 3:
            ans = max(ans, connect[i][0].l + connect[i][1].l + connect[i][2].l)

    for i in range(1, n):
        x, y, l, id = e[i].x, e[i].y, e[i].l, e[i].id
        current = l
        if len(connect[x]) > 1:
            current += connect[x][1].l if connect[x][0].id == id else connect[x][0].l
        if len(connect[y]) > 1:
            current += connect[y][1].l if connect[y][0].id == id else connect[y][0].l
        ans = max(ans, current)

    print(ans)
