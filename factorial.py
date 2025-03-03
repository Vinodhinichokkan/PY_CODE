#------------------Method 1[Using loop]--------------------

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial(5))  #Output: 120

#------------------Method 2--------------------

def factorial(num):
    fact = 1

    for i in range(1, num+1):
        fact *= i
    
    return fact

print(factorial(5))   #Output: 120

#-----------------Method 3[Using Recursion]-----------------

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120

#------------------Method 4 [using built-in function(math)]--------------

import math

print(math.factorial(5))  # Output: 120