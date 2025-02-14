import math


if __name__ == '__main__':
    x = 23333333
    for i in range(10000000, x // 2):
        y = x - i
        if round((y / x) * (math.log2(y / x)) * y + (i / x) * (math.log2(i / x)) * i, 4) == -11625907.5798:
            print(i)
            break