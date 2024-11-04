# example_input:
# 5
# 10234
# 3
# 1 0
# 2 0
# 3 0
# example_output:
# 1

from collections import deque


def main():
    n = int(input())
    s = input().strip()
    k = int(input())
    operations = [tuple(map(int, input().strip().split())) for _ in range(k)]

    result = bfs(n, s, k, operations)
    print(result)


def bfs(n, s, k, operations):
    q = deque([s])
    visited = {s: 0}
    str_sorted = ''.join(sorted(s))

    while q:
        current = q.popleft()
        count = visited[current]
        if current == str_sorted:
            return count

        for x, y in operations:
            t_list = list(current)
            t_list[x], t_list[y] = t_list[y], t_list[x]
            t = ''.join(t_list)

            if t not in visited:
                visited[t] = count + 1
                q.append(t)
    return -1


if __name__ == '__main__':
    main()
