

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

if __name__ == '__main__':
    heap = Heap()
    heap.add(30)
    heap.add(1)
    heap.add(0)
    heap.add(5)
    heap.add(44)
    heap.add(2)
    heap.add(8)
    heap.add(9)
    heap.add(7)
    heap.add(6)

    print(heap.data)

    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
    item = heap.pop()
    print(item,end = "   ")
 
    
    

    