# example_input:
# 3
# example_output:
# 10


if __name__ == '__main__':
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
           ans += (n - i + 1) ** 2
    print(ans)
