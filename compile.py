


from ast import Pass
from multiprocessing.connection import wait

def swapOrder(order,idx):
    while idx+1 < len(order):
        if order[idx][1] > order[idx+1][1] and order[idx][0] ==  order[idx+1][0]:
            order[idx],order[idx+1] = order[idx+1],order[idx]
        idx+=1
    return order

def findCost(order,k,w):
    for item in range(0,len(order)):
        # check if next order comes with same time
        order = swapOrder(order,item)
        curr_order_in_time = order[item][0]
        curr_order_preparation_time =  order[item][1]
        # calc for first order
        if item == 0:
            waiting_time = 0
            total_time_for_completion = curr_order_in_time + curr_order_preparation_time
        else:
            # calc waiting time
            if total_time_for_completion > curr_order_in_time:
                waiting_time = total_time_for_completion - curr_order_in_time
                total_time_for_completion+=curr_order_preparation_time
            else:
                waiting_time  = 0
                total_time_for_completion = curr_order_in_time + curr_order_preparation_time
            # find unit cost per order
        cost =  (k*curr_order_preparation_time) - (w*waiting_time)
        print(cost,end= " ")

order1 = [[3,5],[4,2],[4,1],[4,0],[10,15],[15,2]]
#order1 = [[1,4],[2,2],[9,2],[10,1]]
#findCost(order1,10,1)
print(swapOrder(order1,1))