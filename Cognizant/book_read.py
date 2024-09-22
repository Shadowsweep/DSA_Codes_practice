def max_book_read(A,N):
    A.sort()
    count =0
    total_time =0
    for time in A:
        if total_time + time <= N:
            total_time += time
            count +=1 
    return count 



A=list(map(int,input().split()))
N = int(input())
result = max_book_read(A,N)
print(result)
