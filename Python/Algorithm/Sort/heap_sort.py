from random import randrange,shuffle

def generate_test_list(start,end,count):
    return [randrange(start,end) for i in range(0,count)]

class Heap(object):

    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    @property
    def capacity(self):
        return self.__capacity

    def item(self,index):
        if self.data is None or index >= len(self.data):
            return None
        return self.data[index]
    
    def parent_index(self, index):
        return int((index - 1) / 2)

    def left_child_index(self, index):
        return int(2 * index + 1)
    
    def right_child_index(self, index):
        return int(2 * index + 2)
    
    def parent(self, index):

        if self.data is None or (index < 0 or index >= len(self.data)):
            return None
        
        if self.parent_index(index) < 0:
            return None

        return self.data[self.parent_index(index)]

    def left_child(self,index):

        if self.data is None or (index < 0 or index >= len(self.data)):
            return None
        
        if self.left_child_index(index) < 0:
            return None

        return self.data[self.left_child_index(index)]

    def right_child(self,index):

        if self.data is None or (index < 0 or index >= len(self.data)):
            return None
        
        if self.right_child_index(index) < 0:
            return None

        return self.data[self.right_child_index(index)]

    def last_node(self):
        if self.data is None or len(self.data) == 0:
            return None
        return self.data[len(self.data) - 1]

    def first_node(self):
        if self.data is None or len(self.data) == 0:
            return None
        return self.data[0]

    def add(self,value):
        if value is None: 
            return
        self.data.append(value)
        self.__swap_up()

    def __swap_up(self):
        if self.data is None or len(self.data) == 0:
            return

        current_index = len(self.data) - 1
        parent_index = self.parent_index(current_index)
        while parent_index >= 0 and self.parent(current_index) > self.item(current_index):
            parent_index = self.parent_index(current_index)
            self.data[parent_index] , self.data[current_index] = self.data[current_index], self.data[parent_index]
            current_index = parent_index

    def __swap_down(self,index):

        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)
        min_child_index = left_index
        while (left_index < len(self.data)):

            if right_index < len(self.data) and self.data[right_index] < self.data[left_index]:
                min_child_index = right_index

            if self.data[index] >  self.data[min_child_index]:
                self.data[min_child_index] , self.data[index] = self.data[index], self.data[min_child_index]
                
            index = min_child_index
            left_index = self.left_child_index(index)
            right_index = self.right_child_index(index)
            min_child_index = left_index
  
    def pop(self):
        if self.data is None or len(self.data) == 0:
            return
        first_item = self.data[0]
        self.data[0] , self.data[len(self.data) - 1] = self.data[len(self.data) - 1] , self.data[0]
        del self.data[len(self.data) - 1]
        self.__swap_down(0)
        return first_item

    def __str__(self):
        items = []
        for item in self.data:
            items.append(str(item))
        return " ==> ".join(items)

if __name__ == '__main__':

    test_list = generate_test_list(0,100,50)
    heap = Heap()

    for item in test_list:
        heap.add(item)
   
    print(heap)

    for _ in range(0,len(heap.data)):
        print(heap.pop(),end = "   ")
 
    
    

    