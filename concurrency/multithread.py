# https://medium.com/geekculture/python-multithreading-vs-multiprocessing-da44e62cecd3

import time
import threading
start_time = time.time()

def do_something():
    print('Sleeping 2 seconds')
    time.sleep(2)
    print('Done sleeping ')

thread = []
for _ in range(10):
    t1 = threading.Thread(target=do_something)
    thread.append(t1)
    t1.start()

for t in thread:
    t1.join()

end_time = time.time()

print("Total execution time is : ",end_time-start_time)