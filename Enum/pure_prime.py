def is_prime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    res = 0
    for i in range(2, 20210606):
        temp = str(i)
        if len(temp) == temp.count('2') + temp.count('3') + temp.count('5') + temp.count('7') and is_prime(i):
            res += 1
    print(res)