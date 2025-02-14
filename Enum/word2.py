if __name__ == '__main__':
    s = input()
    char_arr = {}
    for i in s:
        if i in char_arr:
            char_arr[i] += 1
        else:
            char_arr[i] = 1
    res = max(char_arr.values())
    ch = [i for i, count in char_arr.items() if count == res]
    ans = min(ch)
    print(ans)
    print(res)