# Write a code to reverse a string 
# str = "hello"
# rev = str[::-1]
# print(rev)



# # Write a code for factorial

# def factorial(n):
#     if n <= 0 :
#         return -1
#     if n == 1 :
#         return 1 
#     return n * factorial(n-1)




# Write a code for prime number 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num) :
        if num % i ==0 :
            return False
    return True


def prime_number(start,end):
    primes =[]
    for num in range(start , end+1):
        if is_prime(num):
            primes.append(num)
    return primes
    






print(prime_number(10,40))

#Write a code to check if a number is armstrong

def is_armstrong_number(num):
    temp = num
    sum_of_powers = 0
    num_digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    return sum_of_powers == num

print(is_armstrong_number(153))  # True
print(is_armstrong_number(9474))  # True
# print(is_armstrong_number(123))  # False

#second largest
#second smallest
#Remove duplicates
#rotate by k steps
#count_frequency 
#Sorting Methods 
#oops implementation
#searching linear and binary



def second_largest(arr):
    largest , secondd_largest = float('-inf') , float('-inf')
    for num in arr:
        if num > largest:
            secondd_largest = largest
            largest = num
        elif num > secondd_largest and num != largest:
            secondd_largest = num
    return secondd_largest if secondd_largest != float('-inf') else -1

arr = [10,20,30,50,70]
print(second_largest(arr))




def second_smallest(arr):
    smallest,second_smallest = float('inf') , float('inf')
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num<second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else -1

arr = [10,20,30,50,70]
print(second_smallest(arr))
 
    
# Find duplicates in ar
# my_list =  { "name":"Utkarsh Gupta" , "age":25 }

def find_duplicates(arr):
    duplicates= []
    seen =set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates
        



# arr = [10,10,20,30,40,50]
# print(find_duplicates(arr))


#Wac to return reverse of string 
def reversed_string(str) :
    reversed_str =""
    for i in str:
        reversed_str = i + reversed_str
    return reversed_str

print(reversed_string("hello"))



# Wac to rotate by k steps
# def rotate_by_k(arr,k):
#     k %= len(arr)
#     return arr[-k:] + arr[:-k]


def rotate_by_k(arr,k):
    k %= len(arr)
    return arr[-k:] +arr[:-k]

arr = [1,2,3,4,5]
k=2
print(rotate_by_k(arr,k))

def getMax(arr):
    minElement = -1
    for i in range(len(arr)):
        minElement = max(minElement,arr[i])
    
    return minElement

arr=[2,1,4,5,0]
res = getMax(arr)
print(res)


#For palindrome

def check_palindrome(s):
    left , right = 0 , len(s) -1
    while left<=right:
        if s[left]!= s[right]:
            return False
        left += 1
        right -= 1
    return "is palindrome"

s = "madam"
print(check_palindrome(s))


