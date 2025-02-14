if __name__ == '__main__':
    n = int(input())
    force = list(map(int, input().split()))
    a = []
    for i in range(n):
        for j in range(i + 1, n):
            a.append(sum(force[i:j]))
    a.sort()
    result = sum(a)
    for i in range(1, len(a)):
        result = min(abs(a[i] - a[i - 1]), result)
    print(result)