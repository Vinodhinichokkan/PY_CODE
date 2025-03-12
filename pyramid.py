#----------------Pyramid---------------

n = 5
for i in range(1 , n+1):
    print(" " * (n-i)+ "* " * i)


    #  *
  #   * *
  #  * * *
 #  * * * *
#  * * * * *


#--------------Right angle triangle ---------------

n = 5
for i in range(1 , n + 1):
    print("*" * i)


#   *
#   **
#   ***
#   ****
#   *****

#------------inverted right angle------------------

n = 5
for i in range(n, 0, -1):
    print("*" * i)

#   *****
#   ****
#   ***
#   **
#   *

#-----------Diamond-----------------

def pyramid (rows):
    for i in range (rows):
        print(' '*(rows-i-1)+'* '*(i+1))
    for j in range (rows-1, 0, -1):
        print(' '*(rows-j)+'*'*(j))










































