# example_input:
# 4 4
# 2 2 4 4
# 2
# 1 1
# 1 4
# ....
# #.##
# ....
# ....
# example_output:
# YES
from collections import deque


def bfs(n, m, tx, ty, board, directions):
    q = deque([(tx - 1, ty - 1)])
    distance = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    while q:
        cx, cy = q.popleft()
        for x, y in directions:
            cx_to_tx, cy_to_ty = x + cx, y + cy
            if 0 <= cx_to_tx < n and 0 <= cy_to_ty < m:
                if board[cx_to_tx][cy_to_ty] == '#':
                    continue
                if visited[cx_to_tx][cy_to_ty] == 0:
                    q.append((cx_to_tx, cy_to_ty))
                    distance[cx_to_tx][cy_to_ty] = distance[cx][cy] + 1
                    visited[cx_to_tx][cy_to_ty] = 1
    return distance


def main():
    n, m = map(int, input().split())
    sx, sy, tx, ty = map(int, input().split())
    k = int(input())
    monster = [tuple(map(int, input().split())) for _ in range(k)]
    board = [['' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        board[i] = input().strip()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = bfs(n, m, tx, ty, board, directions)
    for mx, my in monster:
        if distance[mx - 1][my - 1] <= distance[sx - 1][sy - 1]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
