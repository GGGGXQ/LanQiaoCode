from collections import deque


def bfs(n, m, tx, ty, board, directions):
    q = deque([(tx-1, ty-1)])
    visited = {(tx - 1, ty - 1)}
    distance = {(tx - 1, ty - 1): 0}

    while q:
        cx, cy = q.popleft()
        for x, y in directions:
            cx_to_tx, cy_to_ty = x + cx, y + cy
            if 0 <= cx_to_tx < n and 0 <= cy_to_ty < m:
                if board[cx_to_tx][cy_to_ty] == '#':
                    continue
                if (cx_to_tx - 1, cy_to_ty - 1) not in visited:
                    visited.add((cx_to_tx, cy_to_ty))
                    distance[(cx_to_tx, cy_to_ty)] = distance[(cx, cy)] + 1
                    q.append((cx_to_tx, cy_to_ty))

    return distance


def main():
    n, m = map(int, input().split())
    sx, sy, tx, ty = map(int, input().split())
    k = int(input())
    monster = [tuple(map(int, input().split())) for _ in range(k)]
    board = [[' ' for _ in range(m)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        board[i] = list(input().strip())

    distance = bfs(n, m, tx, ty, board, directions)
    for mx, my in monster:
        if distance[(mx - 1, my - 1)] < distance[(sx - 1, sy - 1)]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()