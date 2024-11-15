def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(arr))  # Output: 7
