#Iterative Approach

# def find_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# if __name__ == "__main__":  
#     print(find_sum(10))  # 55
    
    
#Recursive Approach
def find_sum(n):
    return n if n == 1 else n + find_sum(n-1)
if __name__ == "__main__":  
    print(find_sum(10))  # 55
