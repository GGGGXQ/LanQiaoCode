from datetime import date


if __name__ == '__main__':
    date1, date2 = input(), input()
    ans = 0

    start_date = date(int(date1[: 4]), int(date1[4: 6]), int(date1[6: ]))
    end_date = date(int(date2[: 4]), int(date2[4: 6]), int(date2[6: ]))

    for y in range(int(date1[: 4]), int(date2[: 4]) + 1):
        d = str(y) + str(y)[::-1]
        try:
            if start_date <= date(int(d[: 4]), int(d[4: 6]), int(d[6: ])) <= end_date:
                ans += 1
        except:
            pass

    print(ans)