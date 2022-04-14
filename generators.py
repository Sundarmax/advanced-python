def simple_generator():
    print("1")
    yield "one"
    print("2")
    yield "two"
    print("3")
    yield "three"

def generator_with_loop():
    def rev_num(A):
        for i in range(len(A)-1,-1,-1):
            yield A[i]
    for num in rev_num([1,2,3,4]):
        print(num)

def generator_expression():
    A = [1,2,3,4,5]
    a  = (num*2 for num in A)
    print(a) # It returns object but not started execution.
    print(next(a))
# represent infinite streams of data
generator_expression()
# generator_with_loop()
# create an object 
# sg = simple_generator()
# print(next(sg))
# print(next(sg))
# print(next(sg))
# sg2 = simple_generator()
# using for loop 
# for i in sg2:
#     print(i)
# print(next(sg))