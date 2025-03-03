list  = [23,65,19,90] 
print(list)

pos1, pos2 = 1 , 3 #65,90

list[pos1],list[pos2] = list[pos2],list[pos1]

print(list)   #[23, 90, 19, 65]