# 3592
# 1 - 1/2 + 1/3 - 1/4 + 1/5...
# example_input:
# 2
# 1 2
# example_output:
# 1.00
# 0.50


if __name__ == '__main__':
    m = int(input())
    list = [int(input()) for i in range(m)]
    for i in range(m):
        num = 0
        line = list[i]
        for j in range(1, line + 1):
            if j % 2 == 1:
                num += 1.0/j
            if j % 2 == 0:
                num -= 1.0/j
        print("%.2f" % num)
