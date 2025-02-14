def get_prime(n):
    result = 0
    m = 2
    while n > 1:
        if n % m != 0:
            m += 1
        else:
            n //= m
            result = max(result, m)
    return result


if __name__ == '__main__':
    n = int(input())
    if get_prime(n) == n:
        ans = -1
    else:
        a = get_prime(n)
        ans = 1e7
        for i in range(n - a + 1, n + 1):
            t = get_prime(i)
            if t == i:
                continue
            ans = min(ans, i - t + 1)

    if ans == 1e7:
        print(-1)
    else:
        print(ans)