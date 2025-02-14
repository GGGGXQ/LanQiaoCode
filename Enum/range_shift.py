def check(x):
    st = 0
    t = arr.copy()
    while t:
        for i in range(len(t)):
            if t[i][0] - x <= st:
                if t[i][0] > st:
                    st = t[i][1] - (t[i][0] - st)
                else:
                    st = max(st, t[i][1] + min(x, st-t[i][0]))
                t.pop(i)
                break
        else:
            return False
    return st >= 10000

def find():
    l = 0
    r = 10 ** 8
    while (r - l) > 1e-8:
        mid = (r + l) / 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort(key=lambda pair:pair[1])
    res = find()
    res = round(res, 1)
    s = str(res)
    t, i = s.split('.')
    if i == '0':
        print(t)
    else:
        print(res)