# 0 , 1 , 1 , 2 , 3 , 5,8
# 0,1,2,3,4,5,6

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(fib(10))
