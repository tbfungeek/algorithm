class Node(object):
    def __init__(self,data,next=None):
        self.__data = data
        self.__next = next
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def __str__(self):
        return str(self.__data)


class Stack(object):
    
    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self,value):
        if value is None:
            return
        node = Node(value)
        #add the node to top of top place
        node.next = self.__top
        #point the top point to node
        self.__top = node
        self.__count += 1

    def pop(self):
        if self.__top == None:
            return
        top_value = self.__top.data
        self.__top = self.__top.next
        return top_value
        self.__count -= 1

    def top(self):
        return self.__top

    def size(self):
        return self.__count
        
    def __str__(self):
        value = []
        for item in self:
            value.append(str(item.data))
        return " ===> ".join(value)

    def __iter__(self):
        current_item = self.__top
        while current_item != None:
            yield current_item
            current_item = current_item.next

if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack)

    print(stack.top())
    print(stack.size())
    
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    