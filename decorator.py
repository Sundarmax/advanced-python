
# decorator without param
from ast import Pass


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

#result = make_pretty(ordinary)
#result()
#ordinary()

# decorator with param
def smart_error(func):
    def check(a,b):
        if b == 0:
            print("Whoops b value is 0, can't divide")
            return 
        return func(a,b)
    return check

@smart_error
def divide(a,b):
    return a/b

print(divide(1,0))

# chaining the decorator
def heading(func):
    def inner(x):
        print("printing heading")
        func(x)
        print("print heading done")
    return inner

def sub_heading(func):
    def inner(y):
        print("printing sub-heading")
        func(y)
        print("printing sub-heading done")
    return inner

@heading
@sub_heading
def print_paragraph(msg):
    print(msg)

#print_paragraph("Johny")