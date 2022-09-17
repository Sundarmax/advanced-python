import imp


import multiprocessing
import time 

def func():  
    start_time = time.time()

    def do_something():
        print('Sleeping 2 seconds')
        time.sleep(2)
        print('Done sleeping ')

    # do_something()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # start
    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    end_time = time.time()
    
    print("Total execution time is : ",end_time-start_time)
    if __name__ == "__main__":
        multiprocessing.freeze_support()
        p1.start()
        p1.join()
func()


# there is some issue with local compiler please do run the same @ onlinegdb compiler. 

# below code is tested in online compiler
