

# def bubble_sort(arr):
#     for i in range(0,len(arr)-1):
#         for j in range(0,len(arr)- 1- i):
#             if arr[j] >arr[j+1]:
#                 arr[j] ,arr[j+1] = arr[j+1] ,arr[j]
#     return arr





def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] ,arr[j]
    
    return arr

arr = [1,5,6,4,9,8,7]
res = bubble_sort(arr)
print(res)

