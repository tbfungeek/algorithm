#!/usr/bin/env python3
#-*-coding:utf-8-*-

import random

def select_sort(list):
    list_length = len(list)
    for i in range(0,list_length - 1):
        for index in range(i+1, list_length):
            if list[index] < list[i]:
                list[index],list[i] = list[i],list[index]
    return list

def random_list(start,stop,length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

if __name__ == "__main__":
    print(select_sort(random_list(2,100,100)));
