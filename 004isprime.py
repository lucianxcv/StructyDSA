'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n): #de la al doilea numar pana la penultimul, 1 si n sunt divizibili ca prime
        if n % i == 0:
            return False

    return True



print(is_prime(1))
O(n) solution, because we check all numbers from 1 to n-1
'''
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1): #de la al doilea numar pana la penultimul, 1 si n sunt divizibili ca prime
        if n % i == 0:
            return False

    return True

print(is_prime(1))   # False
print(is_prime(2))   # True
print(is_prime(77))  # False
print(is_prime(97))  # True