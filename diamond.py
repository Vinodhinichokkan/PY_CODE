#-----------Diamond-----------------

n = 5
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "* " * i)
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "* " * i)


 #   * 
 # * * * 
# * * * * * 
 # * * * 
  #  * 

#--------------number pyramid-----------------

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))


#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5


#----------------pascals triangle---------------

from math import factorial

n = 5
for i in range(n):
    for j in range(n - i + 1):
        print(" ", end="")  
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

#---------------HOLLOW AQUARE-----------------

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#    * * * * *
#    *       *
#    *       *
#    *       *
#    * * * * *      