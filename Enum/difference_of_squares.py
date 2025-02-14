if __name__ == '__main__':
    num_target = [0] * 2022
    for i in range(1, 1011):
        for j in range(i):
            target = (i + j) * (i - j)
            if target <= 2021:
                num_target[target] = 1
    print(num_target.count(1))
