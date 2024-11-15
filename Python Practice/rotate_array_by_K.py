def rotate_array(arr, k):
    k %= len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]
