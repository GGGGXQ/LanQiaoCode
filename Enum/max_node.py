class Node:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

class Trie:
    HIGH_BIT = 31
    def __init__(self):
        self.root = Node()

    def insert(self, val):
        current = self.root
        for i in range(self.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if current.child[bit] is None:
                current.child[bit] = Node()
            current = current.child[bit]
            current.count += 1

    def remove(self, val):
        current = self.root
        for i in range(self.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            current = current.child[bit]
            current.count -= 1

    def max_xor(self, val):
        current = self.root
        ans = 0
        for i in range(self.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if current.child[bit ^ 1] and current.child[bit ^ 1].count > 0:
                ans |= 1 << i
                bit ^= 1
                current = current.child[bit]
        return ans

    def min_xor(self, val):
        current = self.root
        ans = 0
        for i in range(self.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if current.child[bit] and current.child[bit].count > 0:
                current = current.child[bit]
            else:
                ans |= 1 << i
                current = current.child[bit ^ 1]
        return ans

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1

    a = []
    tr = Trie()

    for i in range(n):
        a.append(int(data[idx]))
        tr.insert(a[-1])
        idx += 1

    adj = [[] for _ in range(n)]

    for i in range(n):
        f = int(data[idx])
        idx += 1
        if f != 1:
            adj[i].append(f)
            adj[i].append(i)

    ans = 0
    for i in range(n):
        for v in adj[i]:
            tr.remove(a[v])
        ans = max(ans, tr.max_xor(a[i]))
        for v in adj[i]:
            tr.insert(a[v])
    print(ans)

if __name__ == '__main__':
    solve()