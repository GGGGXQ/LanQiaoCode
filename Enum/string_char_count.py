from collections import defaultdict
if __name__ == '__main__':
    s = input()
    d = defaultdict(lambda : [-1, -1])
    ans = res = 0

    for i, v in enumerate(s):
        ans += i - d[v][1]
        ans -= d[v][1] - d[v][0]
        d[v][0], d[v][1] = d[v][1], i
        res += ans
    print(res)