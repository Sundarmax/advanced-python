# https://medium.com/pragmatic-programmers/using-concurrent-futures-to-run-code-concurren-tly-c319c3486a43
from ast import Pass
import multiprocessing
import concurrent.futures

import time 

start_time = time.time()

def do_something():
    print('Sleeping 2 seconds')
    time.sleep(2)
    return 'Done sleeping '
        
with concurrent.futures.ProcessPoolExecutor() as executor:  
        results = [ executor.submit(do_something) for _ in range(10) ]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
end_time = time.time()

print("Total execution time is : ",end_time-start_time)

# there is some issue with local compiler please do run the same @ onlinegdb compiler.
# below code is tested in online compiler