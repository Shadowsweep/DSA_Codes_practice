

# def reverse_string(s):
#     s = list(s)
#     left , right = 0, len(s) -1 
#     while(left<right):
#         s[left] , s[right] = s[right] , s[left]
#         left += 1
#         right -= 1
#     return ''.join(s)

def reverse_string(s):
    s =list(s)
    left , right  = 0 , len(s) -1
    while left <= right:
        s[left],s[right] = s[right] ,s[left]
        left += 1
        right -= 1
    return ''.join(s)
        

s = "hello"
print(reverse_string(s))