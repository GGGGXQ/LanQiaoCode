# example_input:
# 5
# 2 3 2 4 1
# example_output:
# 4

if __name__ == '__main__':
    n = int(input())
    alist = map(int, input().split())
    b = [0] * int(1e5 + 2)
    for i in alist:
        b[i - 1] += 1
        b[i] += 1
        b[i + 1] += 1
    print(max(b))
