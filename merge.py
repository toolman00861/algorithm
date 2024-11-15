def merge(a, b):
    """合并两个有序数组，返回合并后的有序数组。"""
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_sort(arr):
    """使用归并排序对数组进行排序。"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = [5, 2, 4, 6, 1, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)
