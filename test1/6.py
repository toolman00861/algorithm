from math import sqrt

n = int(input())
a = input().split()
a = [int(i) for i in a]

res = 0
move_times = int(n*(n-1)/2)  # 移动次数
divide_times = 0  # 除以二并向下取整次数

for i in range(n):
    divide_times += a[i].bit_length()

res = move_times + divide_times
print(res)