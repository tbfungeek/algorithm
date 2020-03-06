
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

class Queue(object):
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self,value):
        node = Node(value)
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__count += 1

    def dequeue(self):

        if self.__head is None:
            return None
        #only one element
        if self.__tail == self.__head:
            node = self.__head
            self.__tail = self.__head = None
            self.__count -= 1
            return node
        
        node = self.__head
        self.__head = self.__head.next
        self.__count -= 1
        return node

    def __str__(self):
        value = []
        for item in self:
            value.append(str(item.data))
        return " ====> ".join(value)

    def __iter__(self):
        if self.__head is None:
            return
        current_node = self.__head
        while current_node != self.__tail:
            yield current_node
            current_node = current_node.next
        yield self.__tail

    def size(self):
        return self.__count

if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    