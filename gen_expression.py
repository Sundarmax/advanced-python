from sys import getsizeof

a = [i for i in range(1000) if i %2 == 0]
print(getsizeof(a))
b = (i for i in range(1000) if i %2 == 0)
for i in b:
    print(i)
    break
print(getsizeof(b))