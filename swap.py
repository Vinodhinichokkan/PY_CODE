#----------- Tuple unpacking method-------------------
a = 10;
b = 20;

a,b = b,a

print(a , b)  #20 10

#-------------------using temp-----------------------

a = 10;
b = 20;

temp = a;
a = b;
b = temp;

print(a , b)  #20 10

#--------------------- using arithmetic operators----------------

a = 10;
b = 20;

a = a + b;
b = a - b;
a = a - b;

print (a , b) #20 10

#---------------using bitwise XOR--------------

a = 10;
b = 20;

a = a ^ b;
b = a ^ b;
a = a ^ b;

print(a,b)   #20 #10

