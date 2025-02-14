# 判断1e6能满足多少项
# if __name__ == '__main__':
#     f = [1, 1, 2]
#     for i in range(3, 100):
#         if f[i - 2] + f[i - 1] <= 1e6:
#             f.append(f[i - 2] + f[i - 1])
#         else:
#             print(i) #30
#             break
#     print(f)
#  第31~n的项都需要更改
if __name__ == '__main__':
    f = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
    n = int(input())
    arr = list(map(int, input().split()))
    ans = max(0, n - 30)
    base = []
    for i in range(min(n, 30)):
        base.append(arr[i] / f[i])
    base.sort()
    x = 0
    for i in base:
        count = 0
        for j in base:
            if i - j == 0:
                count += 1
        x = max(x, count)
    ans += min(n, 30) - x
    print(ans)