# First solving using brute force T.C = O n square



def countFreq(arr,n):
    visited = [False] * n 
    for i in range(n):
        if visited[i] == True:
            continue
        count =1
        for j in range(i+1,n):
            visited[j] = True
            count += 1
        print(arr[i],count)


arr = [1,2,2,3,4,4,4,4,7]
n = len(arr)
res = countFreq(arr,n)
print(res)