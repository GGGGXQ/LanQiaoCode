if __name__ == '__main__':
    s = input()
    res = 0
    ch = 'z'
    for i in s:
        cnt = s.count(i)
        if cnt > res:
            res = cnt

    for i in s:
        if s.count(i) == res:
            ch = min(ch, i)

    print(ch)
    print(res)