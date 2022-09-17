from multipledispatch import dispatch

class temp:

    def product(self,x):
        return x

    def product(self,x,y):
        return x*y

s = temp()
# It runs the latest defined method
# print(s.product(2,2))
# The below one throws an error. 
# print(s.product(1))

# It can be done by using disptach 
class temp2:
    @dispatch(int)
    def product(self,x):
        return x*x
    @dispatch(int,int)
    def product(self,x,y):
        return x*y

s2 = temp2()
print(s2.product(2))
print(s2.product(20,20))

@dispatch(int)
def product(x):
    return x*x

@dispatch(int,int)
def product(x,y):
    return x*y

# print(product(2))
# print(product(20,20))