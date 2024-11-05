# example_input:
# 4 4
# 1 1 4 4
# 1100
# 1111
# 1001
# 1111
# example_output:
# 9

from collections import deque


def bfs(n, m, sx, sy, tx, ty, mp):
    q = deque([(sx - 1, sy - 1)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = [[0] * m for _ in range(n)]
    while q:
        cx, cy = q.popleft()
        if cx == tx - 1 and cy == ty - 1:
            return count[cx][cy] + 1

        for x, y in directions:
            cx_to_tx, cy_to_ty = cx + x, cy + y
            if (0 <= cx_to_tx < n and 0 <= cy_to_ty < m and mp[cx_to_tx][cy_to_ty] == 1
                    and count[cx_to_tx][cy_to_ty] == 0):
                q.append((cx_to_tx, cy_to_ty))
                count[cx_to_tx][cy_to_ty] = count[cx][cy] + 1


def main():
    n, m = map(int, input().split())
    sx, sy, tx, ty = map(int, input().split())
    mp = [list(map(int, input())) for _ in range(n)]
    count = bfs(n, m, sx, sy, tx, ty, mp)
    print(n * m - count)


if __name__ == '__main__':
    main()
