# Q2 Max Ballons

def baloon_count(n,x,A,B):
    max_ballons= -float('inf')
    for i in range(n-1):
        for j in range (i+1,n):
            if B[i] + B[j] <= x and A[i] + A[j]>=max_ballons:
                max_ballons = A[i] + A[j]
    
    return max_ballons

n = 4
x=8
A = [4,6,2,7]
B = [5,3,1,6]
max_count = baloon_count(n,x,A,B)
print(max_count)
