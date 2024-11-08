def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [2, 4, 0, 1, 9]
target = 1
print(linear_search(arr, target))  # Output: 3
