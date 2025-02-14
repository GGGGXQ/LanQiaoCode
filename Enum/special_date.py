def add_num(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total

def is_leap(year):
    if (year % 4 == 0 and year% 100 != 0) or year% 400 == 0:
        return True
    return False


if __name__ == '__main__':
    ans = 0
    data = []
    result = {}
    day = [0, 1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    for i in range(1, 32):
        data.append(add_num(i))
    for i in range(1, 13):
        cu_data = add_num(i)
        for j in range(day[i] + 30):
            n_data = cu_data + data[j]
            if n_data not in result:
                result[n_data] = 1
            else:
                result[n_data] += 1

    for i in range(1900, 10000):
        year = add_num(i)
        if year in result:
            ans += result[year]
        if is_leap(i) and year == 13:
            ans += 1

    print(ans)