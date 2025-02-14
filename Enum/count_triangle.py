def distance(a, b, c, d):
    return (a - c) ** 2 + (b - d) ** 2

if __name__ == '__main__':
    n = int(input())
    x = [0] * n
    y = [0] * n
    sp = set()
    count = {}
    for i in range(n):
        x[i], y[i] = map(int, input().split())
        sp.add((x[i], y[i]))

    ans = 0
    line = 0
    for i in range(n):
        for j in range(n):
            if j != i:
                d = distance(x[i], y[i], x[j], y[j])
                ans += count.get(d, 0)
                count[d] = count.get(d, 0) + 1

                dx = (x[i] * 2) - x[j]
                dy = (y[i] * 2) - y[j]

                if (dx, dy) in sp:
                    line += 1
        count.clear()

    print(ans - (line // 2))
