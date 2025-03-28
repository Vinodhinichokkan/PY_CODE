n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

#     *        *
#     **      **
#     ***    ***
#     ****  ****
#     **********
#     ****  ****
#     ***    ***
#     **      **
#     *        *


#--------------FLOYD'S TRIANGLE----------------

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

#  1
#  2 3
#  4 5 6
#  7 8 9 10
#  11 12 13 14 15

#------------------zig-zag--------------

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#  *   * 
#   * *  
#  *   * 
#   * *  
#  *   * 