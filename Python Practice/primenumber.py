# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):  # Check divisors from 2 to num-1
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers_in_range(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# print(prime_numbers_in_range(10, 50))


def is_prime(num):
    if num <2 :
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


def prime_numbers(start,end):
    primes = []
    for num in range(start,end +1):
        if is_prime(num):
            primes.append(num)
    return primes

print(prime_numbers(10,40))