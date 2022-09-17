from time import time

def timer(func):
    def calc():
        start = time()
        res = func()
        end = time()
        print("Total execution time is  : ",end-start)
    return calc

def runLoop():
    for i in range(100000):
        for j in range(1000):
            pass
        
get_time = timer(runLoop)
get_time()