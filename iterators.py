# iterating through itertor
def SampleIterator():
    a = [1,2,3,4] #built in containers in python are iterables. 
    iter_b = iter("SUNDAR")
    iter_a = iter(a)
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))
    # It raises an error 
    # print(next(iter_a))
    def LoopImplementation():
        while True:
            try:
                current = next(iter_b)
                print("curr item is", current)
            except StopIteration:
                print("No more elements in string")
                break
    LoopImplementation()

class CustomIterator:
    def __init__(self,n) -> None:
        self.n = n
    def __iter__(self):
        pass
    # return the numbers between 0 and N
    def __next__(self):
        if self.n > 0:
            curr = self.n
            self.n-=1
            return curr
        else:
            raise StopIteration

def InfiniteIterator():
    a = iter(int,1) # it never returns zero. 
    print(next(a))
    print(next(a))
    print(next(a))

InfiniteIterator()

""" obj = CustomIterator(4)`
obj_iter = obj
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
print(next(obj_iter))
 """
# error 
# print(next(obj_iter))
#SampleIterator()