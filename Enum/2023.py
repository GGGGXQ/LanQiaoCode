if __name__ == '__main__':
    res = 0
    goal = "2023"
    for i in range(12345678, 98765433):
        idx = 0
        for j in str(i):
            if idx != 4 and j == goal[idx]:
                idx += 1
            if idx == 4:
                break
        if idx != 4:
            res += 1
    print(res)