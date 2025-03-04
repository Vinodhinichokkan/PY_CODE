#--------------Method 1[using count]for small lists---------------

list = [1, 2, 3, 4, 2, 2, 5, 6, 2]

count = list.count(2)
print(count)  # Output: 4

#----------------Method 2[using counter]----------------
from collections import Counter

my_list = [1, 2, 3, 4, 2, 2, 5, 6, 2]

counter = Counter(my_list)
print(counter[2])  # Output: 4