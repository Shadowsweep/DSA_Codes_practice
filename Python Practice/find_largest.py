
# first finding the min 

# def getMin(arr):
#     minElement = float('inf')
#     for i in range(len(arr)):
#         minElement = min(minElement,arr[i])
#     return minElement

# arr =[2,1,4,5,0]
# res = getMin(arr)
# print(res)

def getMax(arr):
    minElement = -1
    for i in range(len(arr)):
        minElement = max(minElement,arr[i])
    
    return minElement

arr=[2,1,4,5,0]
res = getMax(arr)
print(res)