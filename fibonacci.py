# fibonacci-----> a series of numbers in which each number is the sum of the two preceding numbers--------

#------------------------Method 1-------------------
n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range (2 , 10):
    sum = n1 + n2
    print(sum)

    n1 = n2
    n2 = sum

#output

'''
0
1
1
2
3
5
8
13
21
34
'''

#-----------------Method 2[Using yield generator]------------------

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example
print(list(fibonacci(10)))