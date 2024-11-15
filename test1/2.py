n = int(input())
str1 = input()
remove_str = ['%', '&', '*', '?', '@', '^']
for i in remove_str:
    str1 = str1.replace(i, '')

if str1 == "DGUT":
    print("YES")
else:
    print("NO")
