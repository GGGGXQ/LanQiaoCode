if __name__ == '__main__':
    ans = 0
    line = []
    for x1 in range(20):
        for y1 in range(21):
            for x2 in range(20):
                for y2 in range(21):
                    if x1 == x2 or y1 == y2:
                        continue
                    k = (y2 - y1) / (x2 - x1)
                    b = (x2 * y1 - x1 * y2) / (x2 - x1)
                    if (k, b) not in line:
                        ans += 1
                        line.append((k,b))
    print(ans + 20 + 21)
