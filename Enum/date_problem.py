from datetime import *


def check(year, month, day):
    if 60 <= year <= 99:
        year += 1900
    elif 0 <= year <= 59:
        year += 2000
    else:
        return False
    try:
        t_date = date(year, month, day)
    except:
        return False
    return str(t_date)


if __name__ == '__main__':
    a, b, c = map(int, input().split('/'))
    res = set()
    if check(a, b, c):
        res.add(check(a, b, c))
    if check(c, a, b):
        res.add(check(c, a, b))
    if check(c, b, a):
        res.add(check(c, b, a))
    if res:
        print('\n'.join(sorted(list(res))))
