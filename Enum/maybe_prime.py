# 3334
# example_input:
# 5
# example_output:
# 3


from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    ans = 0
    n = int(input())
    for i in range(2, n + 1):
        a = 0
        while i != 0:
            a += i % 10
            i //= 10
        if is_prime(a):
            ans += 1
    print(ans)
# 2 over time in test
