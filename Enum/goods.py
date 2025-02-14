if __name__ == '__main__':
    n = 2021041820210418
    num = []
    res  = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            num.append(i)
            if i != n / i:
                num.append(int(n / i))

    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] * num[j] > n:
                continue
            for k in range(len(num)):
                if num[i] * num[j] * num[k] == n:
                    res += 1
    print(res)
