def check(month, day):
    if month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month == 2 and day > 28:
        return False
    v = [4, 6, 9, 11]
    for i in v:
        if month == i and day > 30:
            return False
    return True

def find(month, day, a):
    v = []
    if day < 10:
        v.append(day)
        v.append(0)
    else:
        while day > 0:
            v.append(day % 10)
            day //= 10
    if month < 10:
        v.append(month)
        v.append(0)
    else:
        while month > 0:
            v.append(month % 10)
            month //= 10
    v.append(3)
    v.append(2)
    v.append(0)
    v.append(2)
    v.reverse()
    idx = 0
    for i in range(100):
        if idx != 8 and a[i] == v[idx]:
            idx += 1
        if idx == 8:
            return True
    return False


if __name__ == '__main__':
    s = "5 6 8 6 9 1 6 1 2 4 9 1 9 8 2 3 6 4 7 7 5 9 5 0 3 8 7 5 8 1 5 8 6 1 8 3 0 3 7 9 2 7 0 5 8 8 5 7 0 9 9 1 9 4 4 6 8 6 3 3 8 5 1 6 3 4 6 7 0 7 8 2 7 6 8 9 5 6 5 6 1 4 0 1 0 0 9 4 8 0 9 1 2 8 5 0 2 5 3 3"
    a = list(map(int, s.split()))
    ans = 0
    for i in range(1, 13):
        for j in range(1, 32):
            if check(i, j):
                if find(i, j, a):
                    ans += 1
    print(ans)
