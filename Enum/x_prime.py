from itertools import combinations


def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    x_prime = set()
    for i in range(1000001):
        i_str = str(i)
        M = len(i_str)

        for K in range(M):
            result = set()
            for positions in combinations(range(M), K):
                result_char = []
                for index in range(M):
                    if index not in positions:
                        result_char.append(i_str[index])
                result_str = ''.join(result_char)
                result.add(int(result_str))
            for p in result:
                if is_prime(p):
                    x_prime.add(i)
                    break
    print(len(x_prime))
