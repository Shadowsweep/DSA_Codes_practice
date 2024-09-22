# Count even sum in odd elements in rows 
def sum_even(r,c,M):
    count=0
    for i in range(r):
        sum= 0
        for j in range(c):
            if M[i][j] %2 !=0  :
                sum += M[i][j]
                if sum>0 and sum%2==0:
                    count+= 1
    return count

r=3
c=2
M = [[2,4],[0,0] ,[11,11]]
count_ans = sum_even(r,c,M)
print(count_ans)

