#-*-coding:utf8-*-
#!/usr/bin/env python3

import random
import math

class ArrayWrapper(object):

    def __init__(self,capacity):
        super().__init__()
        self.data = []
        self.capacity = capacity

    def __getitem__(self,position):
        if position >= len(self.data) or position < 0:
            return None
        else:
            return self.data[position]

    def __setitem__(self,position,value):
        if position > len(self.data) or position < 0:
            return
        else:
            self.data[position] = value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item
    
    def contain(self,value):
        for item in self.data:
            if item == value:
                return True
        return False

    def delete(self,position):
        if position >= len(self.data) or position < 0:
            return False
        else:
            self.data.pop(position)
            return True

    def insert(self, position, value):
        if len(self.data) > self.capacity:
            return False
        else:
            return self.data.insert(position,value)
    
    def findObject(self, position):
        if position >= len(self.data) or position < 0:
            return None
        else:
            return self.data[position]

    def description(self):
        for item in self:
            print(item)

if __name__ == '__main__':
    
    #test init
    array = ArrayWrapper(10)

    #test insert
    for index in range(0,10):
        array.insert(index,index)
  
    #test __getitem__
    print(array[0])
    print(array[5])
    print(array[3])

    #test __setitem__
    array[0] = 10000
    array.description()

    #test __iter__
    for value in array:
        print(value)

    #test contain
    print(array.contain(9))

    #test findObject
    print(array.findObject(4))

    #test delete
    array.delete(4)
    print(array.findObject(4))
    
    
