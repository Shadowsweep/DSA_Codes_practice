

def selection_sort(arr):
    for i in range(0,len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex!=i:
            arr[i] , arr[minIndex] = arr[minIndex] ,arr[i]
    return arr


arr = [1,5,6,4,9,8,7]
res = selection_sort(arr)
print(res)

