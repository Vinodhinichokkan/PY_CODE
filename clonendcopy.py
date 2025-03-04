#--------------Method 1[using slicing technique]---------------

list = [4, 8, 2, 10, 15, 18]

list_copy = list[:]

print(list_copy)

#---------------method 2[using extend method]---------------


list = [4, 8, 2, 10, 15, 18]

list_copy = []

list_copy.extend(list)

print(list_copy)

#---------------Method 3[using list() method]--------------------------

#list = [4, 8, 2, 10, 15, 18]

#list_copy = list(list)

#print(list_copy)

#-------------Method 4[using copy()]-----------------------

list = [4, 8, 2, 10, 15, 18]

list_copy = list.copy()

print(list_copy)

#-------------Method 5[using list comprehension]-----------------------
list = [4, 8, 2, 10, 15, 18]

list_copy = [i for i in list]

print(list_copy)

