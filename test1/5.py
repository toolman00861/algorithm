n = int(input())
s = input()
t = input()


# 将s中的第l到第r个字符进行反转使得s==t
def reverse_str(s_: str, L, r):
    res = s_[:L - 1] + s_[L - 1:r][::-1] + s_[r:]
    return res


def check(s_, t_):
    global best_i, best_j, dist
    # 找到第一个不相同的位置：
    x = 0
    y = n - 1
    while x < n and s_[x] == t_[x]:
        x += 1
    while y >= 0 and s_[y] == t_[y]:
        y -= 1
    if x > y:
        # 一定会给出不同的两个字符串
        return

    if reverse_str(s_, x+1, y+1) == t_:
        # 翻转后相等
        best_i = x+1
        best_j = y+1
        dist = x - y


best_i = -1
best_j = -1
dist = 100000
check(s, t)
if best_i == -1 or best_j == -1:
    print('NO')
else:
    print(best_i, best_j)
