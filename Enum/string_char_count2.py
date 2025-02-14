if __name__ == '__main__':
    s = input()
    left = [-1 for i in range(26)]
    count = 0
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        count += (len(s) - i) * (i - left[index])
        left[index] = i
    print(count)