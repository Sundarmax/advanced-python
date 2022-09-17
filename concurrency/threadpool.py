import time
import concurrent.futures

start = time.time()
def go_sleep(sec):
    print('Sleep {} sec(s)'.format(sec))
    time.sleep(sec)
    return 'Done sleep {}'.format(sec)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 4, 3, 2, 5,6,7,8,9,10]
    # results = [executor.submit(go_sleep, sec) for sec in secs]
    results = executor.map(go_sleep, secs)
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
finish = time.time()
print('Finished in {} second(s)'.format(round(finish-start, 2)))


# https://engineering.contentsquare.com/2018/multithreading-vs-multiprocessing-in-python/
# https://medium.com/mindful-engineering/multithreading-multiprocessing-in-python3-f6314ab5e23f

