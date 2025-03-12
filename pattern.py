rows = 6
for i in range (rows):
    for j in range (i):
        print(i , end = ' ')
print('')


#-------------------print python---------

string = "python"
x = 0
for i in string:
    x = x + 1
    print(string[0:x])
for i in string:
    x = x - 1
    print(string[0:x])

#   p
#   py
#   pyt
#   pyth
#   pytho
#   python
#   pytho
#   pyth
#   pyt
#   py
#   p 