#---------Method 1[Temporary variable]--------------

list = [12,35,9,56,24]

size = len(list)  # 5

temp = list[0]

list[0] = list[size-1]

list[size-1] = temp

print("list after swapping:", list)  #list after swapping: [24, 35, 9, 56, 12]

#-----------Method 2--------------

list = [12,35,9,56,24]

list[0] , list[-1] = list[-1] , list[0]

print("list after swapping:", list)  #list after swapping: [24, 35, 9, 56, 12]

#-----------method 3 [using Tuple]----------

list = [12,35,9,56,24]

get = (list[-1] , list[0])
list[0] , list[-1] = get 

print("list after swapping:", list)  #list after swapping: [24, 35, 9, 56, 12]

#--------method 4 [ using *operand]----------------

list = [12,35,9,56,24]

start, *middle, end = list
list = [end, *middle, start]

print("list after swapping:", list)  #list after swapping: [24, 35, 9, 56, 12]

#---------method 5 [using pop]-------------------

list = [12,35,9,56,24]

first = list.pop(0)
last = list.pop(-1)

list.insert(0,last)
list.append(first)

print("list after swapping:", list)  #list after swapping: [24, 35, 9, 56, 12]

