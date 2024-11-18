


# arr = [1,2,3,4,5]
# res = arr[::-1]
# print(res)



# ss = 'Hello'
# rs = ss[::-1]
# print(rs)

# def getReverse(arr):
#     n=  len(arr)
#     start =0
#     end =  n-1
#     while start <= end:
#         arr[start], arr[end] = arr[end] , arr[start]
#         start += 1
#         end -=1
#     print(arr)


# arr = [5,4,3,2,1]
# res= getReverse(arr)
# print(res)



def getReverse(arr):
    start =0
    end = len(arr)-1
    while start <= end:
        arr[start] , arr[end]  = arr[end] ,arr[start]
        start +=1 
        end -=1
    print(arr)

arr =[5,4,3,2,1]
res = getReverse(arr)
print(res)