# last_version is time_out

n = int(input())
energies = list(map(int, input().split()))
max_energy = max(energies)


def check(index):
    now_energy = energies[index]
    next_index = (index + 1) % n
    while next_index != index:
        if now_energy > energies[next_index]:
            now_energy *= 2
            if now_energy > max_energy:
                return True
        else:
            return False
        next_index = (next_index + 1) % n
    return True


if __name__ == '__main__':
    for i in range(n):
        if check(i):
            print(1)
        else:
            print(0)
