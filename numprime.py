#----------------Method 1-----------------

num = 8;
count = 0;

if num > 1:
    for i in range (1 , num + 1):
       if (num % i) == 0:
           count = count + 1
    
    if count == 2:
         print("Number is prime")
    else:
         print("Number is not prime")  # number is not prime.

#-----------------Method 2---------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(11))  # Output: True
print(is_prime(10))  # Output: False