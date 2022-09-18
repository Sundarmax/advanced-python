import array 
# integer 2 bytes 
# float 4 bytes.

a = array.array('i',[2,3,4])

a.append(5)

# error 
# a.append(6.4)

b = array.array('f',[2.5,2])
print(b)
b.pop(1) # remove item at given index
print(b)
