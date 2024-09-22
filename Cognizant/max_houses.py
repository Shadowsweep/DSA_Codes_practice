def max_house(A, N):
    count = 0
    i = 1  # Start from the first house (index 0)
    
    while i < N:
        i += A[i-1]  # Jump to the next house based on the value in A[i]
        count += 1  # Increment the count for each valid house visit
    
    return count


A = list(map(int, input().split()))
N = len(A)
result = max_house(A, N)
print(result)
