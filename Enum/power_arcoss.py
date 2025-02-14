def add_base_num(x, base):
    sums = 0
    while x:
        sums += x % base
        x //=  base
    return sums

if __name__ == '__main__':
    res = 0
    for i in range(1, 2025):
        if add_base_num(i, 2) == add_base_num(i, 4):
           res += 1
    print(res)