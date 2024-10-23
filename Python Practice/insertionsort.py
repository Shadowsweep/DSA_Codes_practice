# insertion sort 

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        while arr[j] > arr[j+1] and j>=0:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
            j -=1
    return arr


arr = [1,5,6,4,9,8,7]
res = insertion_sort(arr)
print(res)


# Optimalest solution
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         curNum = arr[i]
#         for j in range(i-1,0,-1):
#            if arr[j] > curNum:
#                arr[j+1] = arr[j]
#            else:
#                arr[j+1] = curNum
#                break
#     return arr

# arr = [1,5,6,4,9,8,7]
# res = insertion_sort(arr)
# print(res)
