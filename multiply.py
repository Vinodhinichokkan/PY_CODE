#------------------Method 1 [using functools.reduce()]-----------------

from functools import reduce

my_list = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, my_list)
print(result)                                     # Output: 120

#---------------Method 2 [math.prod()]

import math

my_list = [1, 2, 3, 4, 5]
print(math.prod(my_list))                          # Output: 120