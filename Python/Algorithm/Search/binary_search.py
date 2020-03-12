#!/usr/bin/env python3
#-*-coding:utf-8-*-

import time
import functools

def excute_time(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s: begin excute =====> "%(tag))
            begin_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print("%s: result: %s"%(tag,str(result)))
            print("%s: excute time =====> [%f ms]"%(tag,(end_time - begin_time) * 1000))
            return result
        return wrapper
    return decorator

@excute_time("binary_search")
def binary_search(list,item):
    if len(list) == 0:
        return -1;
    hight = len(list)
    low   = 0

    while low <= hight:
        mid_index = int((hight + low) / 2);
        mid_value = list[mid_index]
        if item < mid_value:
            hight = mid_index - 1
        elif item > mid_value:
            low = mid_index + 1
        else:
            return mid_index
    return -1 

if __name__ == "__main__":
    binary_search([1,2,4,5,6,7,8,78],4)
    