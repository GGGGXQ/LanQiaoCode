if __name__ == '__main__':
    num = int(input())
    arr = input()
    result = 0
    for i in range(num):
        ticket = 0
        count = 1
        num_arr = list(map(int, arr.split()))
        while num_arr and count <= max(num_arr):
            if num_arr[i] == count:
                ticket += num_arr.pop(i)
                count = 1
                if len(num_arr) == 0:
                    break
                i = i % len(num_arr)
            else:
                count += 1
                i = (i + 1) % len(num_arr)
        if ticket > result:
            result = ticket
    print(result)