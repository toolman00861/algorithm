n = int(input())
a = input().split()

plus_num = int(n / 2 + 0.5)
minus_num = int(n / 2)

a = [int(i) for i in a]
a.sort()

res = 0
j = 0
for i in range(minus_num):
    res -= a[i]
    j += 1

for i in range(plus_num):
    res += a[j]
    j += 1

print(res)
