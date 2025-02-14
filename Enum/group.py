if __name__ == '__main__':
    A = list(map(str,input().split(",")))
    B = list(map(str,input().split(",")))
    C = list(map(str,input().split(",")))
    sum = 0
    for i in A:
        if i in B and i not in C:
            sum += 1
    print(sum)
