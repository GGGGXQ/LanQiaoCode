def get_prime(num):
    lst = []
    p = 2
    while p * p < num:
        if num % p == 0:
            lst.append(p)
            while num % p == 0:
                num //= p
        p += 1
    if num > 1:
        lst.append(num)
    return lst


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    first_meet_index = {}
    best = (n, n)

    for index, num in enumerate(nums):
        if num == 1:
            continue
        primes_lst = get_prime(num)
        meeted_primes = [first_meet_index[p] for p in primes_lst if p in first_meet_index]

        if meeted_primes:
            i = min(meeted_primes)
            j = index
            if (i, j) < best:
                best = (i, j)

        for p in primes_lst:
            first_meet_index.setdefault(p, index)

    print(best[0] + 1, best[1] + 1)