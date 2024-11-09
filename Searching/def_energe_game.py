def solve():
    n = int(input())
    energies = [0] + list(map(int, input().split()))
    max_energy = max(energies)
    for i in range(1, n + 1):
        out_list = [0] * (n + 1)
        if dfs(n, i, energies, max_energy, out_list):
            print(1)
        else:
            print(0)


def dfs(n, index, energies, max_energy, out_list):
    if index == n:
        first = next_index(1, out_list)
        if energies[index] > energies[first]:
            return True
        else:
            return False

    find_next = next_index(index + 1, out_list)
    while find_next != index:
        if energies[index] > energies[find_next]:
            energies[index] *= 2
            out_list[find_next] = -1
            if energies[index] > max_energy:
                return True
            find_next = next_index(find_next, out_list)
        else:
            return False


def next_index(find_index, out_list):
    while out_list[find_index] == -1:
        find_index += 1
    return find_index


if __name__ == '__main__':
    solve()
