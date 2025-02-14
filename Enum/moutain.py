if __name__ == '__main__':
    ans = 0
    for i in range(22, 20000):
        s = list(str(i))
        if sorted(s) == s:
            ans += 1

    for i in range(11, 10000):
        s = list(str(i))
        if sorted(s) == s:
            ans += 10 - int(max(s))
    print(ans)