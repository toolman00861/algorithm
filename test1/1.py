n = int(input())
first_arr = input().split()
first_arr = [int(i) for i in first_arr]

second_arr = input().split()
second_arr = [int(i) for i in second_arr]

for i in range(n):
    if first_arr[i] == second_arr[i]:
        continue
    elif first_arr[i] > second_arr[i]:
        print("first")
        exit()
    else:
        print("second")
        exit()
print("undecidable")
