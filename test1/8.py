from collections import deque


class Num:
    def __init__(self, num, index):
        self.num = num
        self.index = index

    def __lt__(self, other):
        return self.num < other.num


n, k = map(int, input().split())
a = input().split()
a_list = [Num(int(a[i]), i) for i in range(n)]
a_list.sort(reverse=True)

b = input().split()
b_list = [Num(int(b[i]), i) for i in range(n)]
b_list.sort(reverse=True)

# 贪心寻找出k个数字，保证res最大,a,b至少选出一种
res = 0
index_set = set()
a_chosen = False
b_chosen = False
i = 0
j = 0
for x in range(k):
    # 确保a_list[i]和b_list[j]不在index_set中
    while i < n and a_list[i].index in index_set:
        i += 1
    while j < n and b_list[j].index in index_set:
        j += 1
    # 结尾检查a, b 是否都被选过
    if x == k-1:
        if not a_chosen:
            res += a_list[i].num
            break
        if not b_chosen:
            res += b_list[j].num
            break

    if a_list[i].num > b_list[j].num:
        res += a_list[i].num
        index_set.add(a_list[i].index)
        i += 1
        a_chosen = True
    else:
        res += b_list[j].num
        index_set.add(b_list[j].index)
        j += 1
        b_chosen = True

print(res)
