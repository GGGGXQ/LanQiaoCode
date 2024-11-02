# example_input:
# 3
# 3 3 1
# example_output:
# 4


if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().split()))
    list.sort(reverse=True)

    order_list = [0] * n
    number = 1
    for i in range(n):
        if i > 0 and list[i] < list[i-1]:
            number = i + 1
        order_list[i] = number

    total_bonus = sum(n - no for no in order_list)
    print(total_bonus)
