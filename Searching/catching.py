from collections import deque


def main():
    n, m = list(map(int, input().split()))
    sx, sy, tx, ty = list(map(int, input().split()))
    tx, ty = tx - 1, ty - 1
    k = int(input())
    monster = {}
    visited = set()

    for i in range(k):
        mx, my = list(map(int, input().split()))
        mx, my = mx - 1, my - 1
        visited.add((mx, my))
        monster[i] = deque([(mx, my)])
    for i in range(n):
        for j, v in enumerate(list(input())):
            if v == '#':
                visited.add((j, j))

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    bfs(n, m, sx, sy, tx, ty, k, directions, visited, monster)


def bfs(n, m, sx, sy, tx, ty, k, directions, visited, monster):
    person_next = deque([(sx - 1, sy - 1)])
    while person_next:
        person_cost = 0
        person_x, person_y = person_next.popleft()
        visited.add((person_x, person_y))
        for x, y in directions:
            person_to_x, person_y = x + person_x, y + person_y
            if person_x == tx and person_y == ty:
                if (person_x, person_y) not in visited:
                    print("YES")
                else:
                    print("NO")
                return
            new_cost = abs(person_x - tx) + abs(person_y - ty)
            if 0 <= person_x < n and 0 <= person_y < m and (person_x, person_y) not in visited:
                if person_cost == 0 or new_cost < person_cost:
                    person_cost = new_cost
                    person_next.append((person_x, person_y))

        for m in monster:
            monster_cost = 0
            monster_x, monster_y = monster[m].popleft()
            visited.add((monster_x, monster_y))
            for x, y in directions:
                monster_to_x, monster_to_y = x + monster_x, y + monster_y
                if monster_to_x == person_x and monster_to_y == person_y:
                    print("NO")
                    return
                new_cost = abs(monster_x - tx) + abs(monster_y - ty)
                if 0 <= monster_to_x < n and 0 <= monster_to_y < m:
                    if monster_cost == 0 or new_cost < monster_cost:
                        monster_cost = new_cost
                        monster[m].append((monster_x, monster_y))
    print("NO")


if __name__ == '__main__':
    main()
