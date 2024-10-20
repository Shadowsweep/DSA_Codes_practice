def switch_pens(A, n):
    count = 0
    for i in range(n - 1):  # Loop through the indices from 0 to n-2
        if A[i] % 2 != 0 and A[i + 1] % 2 == 0:  # Check if A[i] is odd and A[i+1] is even
            count += 1  # Increment count if the condition is met
    return count


n = 6
A = [70, 23, 13, 26, 72, 19]
count_pens = switch_pens(A, n)
print(count_pens)

