from collections import deque


class Num:
    def __init__(self, num, index, sym):
        self.num = num
        self.index = index
        self.sym = sym

    def __lt__(self, other):
        return self.num < other.num


n, k = map(int, input().split())
a = input().split()
a = [int(a[i]) for i in range(n)]

b = input().split()
b = [int(b[i]) for i in range(n)]

c = list(Num for i in range(n))
for i in range(n):
    if a[i] > b[i]:\

        c[i] = Num(a[i], i, 'a')
    else:
        c[i] = Num(b[i], i, 'b')
c.sort(reverse=True)
# 贪心寻找出k个数字，保证res最大,a,b至少选出一种
res = 0
a_chosen = False
b_chosen = False
i = 0
for x in range(k):
    if x == k - 1:
        index = c[i].index
        if not a_chosen:
            res += a[index]
            break
        if not b_chosen:
            res += b[index]
            break
    res += c[i].num
    if c[i].sym == 'a':
        a_chosen = True
    if c[i].sym == 'b':
        b_chosen = True
    i += 1

print(res)
