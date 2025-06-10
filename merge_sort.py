def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        while left and right:
            result.append((left.pop(0) if left[0] <= right[0] 
                           else right.pop(0)))
        return result + left + right

    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

print(merge_sort([9, 3, 5, 1, 4, 8, 2, 7]))
