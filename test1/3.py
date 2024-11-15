def func(a, i, res):
    res1 = res + int(a[i][0])
    res2 = res + int(a[i][1])
    if i == 9:
        return res1 == 20 or res2 == 20
    first = func(a, i + 1, res1)
    second = func(a, i + 1, res2)
    if first or second:
        return True
    return False


a = input().split()
if func(a, 0, 0):
    print("YES")
else:
    print("NO")
