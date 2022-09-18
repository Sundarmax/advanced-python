# takes iterables and aggregate them and return it.
a = ['x','y','z']
b = [1,2,3]
# zip
c = list(zip(a,b))
print(c)

# unzip
g,h = zip(*c)
print(g,h)

# what if they have different length
numbersList = [1, 2, 3]
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
numbers_pair = list(zip(numbersList,numbers_tuple))
print(numbers_pair)

# zip to dict

a1 = [1,2,3]
a2 = ["O","T","Th"]
c1 = dict(zip(a1,a2))
print(c1)

d1,d2 = zip(*c1.items())
print(d1,d2)

