def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(array_intersection(arr1, arr2))  # Output: [3, 4]
