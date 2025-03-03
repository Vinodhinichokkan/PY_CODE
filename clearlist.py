#---------------Method 1[using clear]---------------

list = [6 , 0 , 4 , 1]
print(list)

list.clear()
print(list)

#------------------Method 2[list with no value]-------

list = [6 , 0 , 4 , 1]
print(list)

list = []
print(list)

#----------------Method 3[using "*=0"]---------this method removes all the elements

list = [6 , 0 , 4 , 1]
print(list)

list *=0  #delete list
print(list) #

#------------Method 4[using del]----------------

list = [6 , 0 , 4 , 1]
print(list)

del list[:]
print(list)