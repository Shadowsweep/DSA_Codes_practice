# num = input('Number :')
# print(float(num) - 5  )

# hello = 'hello'
# print(type(hello))

# for i in range(10,2, -1):
#     print(i)

# x = [3,4,55,3,2,4]
# for i in range(len(x)):
#     print(x[i])

# x = [0,2,3,4,5,6,7,8]
# y = ['hi','hello','goodbye','cya','sure']
# s = "hello"

# sliced = x[start:stop:step]
# print (sliced)

# x = {'key': 4}
# print(x['key'])

# def func(*args,**kwargs):
#     pass
# x = [1,23,2363,22]
# print(*x)
# print(x)

def func(x,y):
    print(x,y)
pairs = [(1,2),(3,4)]

for pair in pairs:
    # func(pair[0],pair[1])
    # func(*pair) (This is pythonic way to do for tuples)
    # func(**{'x':2,'y':5}) this is used for dictionary 
    func(**{'x':2,'y':5})
    
#  args -  Normal arguments 
#  kwargs - keyword Arguments 

# Lambda Function

x = lambda x: x + 5
print(x(2))
x1 = f'hello {6 +8 }'
print(x1)