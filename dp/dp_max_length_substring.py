def change(str):
    temp = ''
    str_list = []
    for i in str:
        if 'A' <= i <= 'Z':
            if temp != '':
                str_list.append(temp)
                temp = ''
        temp += i
    str_list.append(temp)
    return str_list


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    change_string1 = change(string1)
    change_string2 = change(string2)

    len1 = len(change_string1)
    len2 = len(change_string2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1):
        for j in range(len2):
            if change_string1[i] == change_string2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    print(dp[-1][-1])
