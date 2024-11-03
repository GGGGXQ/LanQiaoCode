# example_input:
# 3 2
# 3 2 1
# 1 2
# example_output:
# YES


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    b = sorted(a)

    for _ in range(n):
        for j in p:
            if j > n or j + 1 > n:
                continue
            elif a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]

    if a == b:
        print('YES')
    else:
        print('NO')
