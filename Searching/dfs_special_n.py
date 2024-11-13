N = 100000
ans = [0] * (N + 1)
pre = [0] * (N + 1)
choice = []


def dfs(count, index, multiple_sum, addsum):
    if count == n:
        if check(addsum):
            ans[multiple_sum] += 1
        return

    for i in range(index, N + 1):
        if multiple_sum * pow(i, n - count) > N:
            break
        choice.append(i)
        dfs(count + 1, i + 1, multiple_sum * i, addsum + i)
        choice.pop()


def check(addsum):
    for i in range(len(choice)):
        temp = addsum - choice[i]
        if temp <= choice[i]:
            return False
    return True


if __name__ == '__main__':
    t, n = map(int, input().split())
    dfs(0, 1, 1, 0)
    pre[0] = 0
    for i in range(1, N + 1):
        pre[i] = pre[i - 1] + ans[i]

    while t > 0:
        l, r = map(int, input().split())
        print(pre[r] - pre[l - 1])
        t -= 1
