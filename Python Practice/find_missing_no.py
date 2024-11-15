def find_missing_number(arr, n):
    total = n * (n + 1) // 2  # Sum of first n numbers
    return total - sum(arr)

# Example
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr) +1 
print(find_missing_number(arr, n))  # Output: 5

