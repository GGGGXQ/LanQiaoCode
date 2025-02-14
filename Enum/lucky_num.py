def check_ha(x, base):
    current = x
    total = 0
    while current:
        total += current % base
        current = current // base
    return x % total == 0


if __name__ == '__main__':
    res = 0
    for i in range(1, 1000000):
        if check_ha(i, 2) and check_ha(i, 8) and check_ha(i, 10) and check_ha(i, 16):
            res += 1
        if res == 2023:
            print(i)
            break
