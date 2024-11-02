# example_input:
# 2
# 1 3 2 4
# 2 5 3 6
# example_output:
# 6
# 10

def solve():
    a, b, c, d = map(int, input().strip().split())
    ans = 0
    for i in range(a, b + 1):
        if i < c:
            ans += d - c + 1
        elif i < d:
            ans += d - i
    print(ans)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        solve()