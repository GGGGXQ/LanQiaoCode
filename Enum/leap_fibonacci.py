def fibonacci(num):
    s = []
    while num != 0:
        s.append(num % 10)
        num //= 10
    return s[::-1]

def is_leap_fibonacci(num):
    s = fibonacci(num)
    while num >= s[-1]:
        if num in s:
            return True
        else:
            s.append(sum(s))
            s = s[1:]
    return False

if __name__ == '__main__':
    for i in range(10000000, 0, -1):
        if is_leap_fibonacci(i):
            print(i)
            break