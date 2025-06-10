def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([9, 3, 5, 1, 4, 8, 2, 7]))
# Output: [1, 2, 3, 4, 5, 7, 8, 9]