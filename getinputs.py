import findingmax
arraylen = input ('enter number of elements to find max no of')
array = []
i = 0
while (int(i)<int (arraylen)):
    array.append ( int ( input (f"enter {i}th element") ) )
    i = int(i)+1
print (findingmax.findmaxno(array))    
