if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        max_num = arr[i]
        min_num = arr[i]
        for j in range(i, n):
            if arr[j] > max_num:
                max_num = arr[j]
            if arr[j] < min_num:
                min_num = arr[j]
            if max_num - min_num == j - i:
                res += 1
    print(res)